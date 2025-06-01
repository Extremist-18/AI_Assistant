from __future__ import print_function
import datetime
from datetime import timedelta
import dateparser
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import sys
sys.path.insert(0,'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak

SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/gmail.send'
]
def get_calendar_service():
    creds = None
    if os.path.exists('token.json'):
        try:
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        except Exception as e:
            print("Invalid token.json file. Deleting and resetting auth.")
            os.remove('token.json')
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                print("Refresh failed. Deleting token.json.")
                os.remove('token.json')
                return get_calendar_service()
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join('features', 'credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service

def create_event(service, command):
    import re

    text = command.lower().replace("remind me to", "").strip()

    # Try to split the action and time using regex to find time patterns
    # This looks for "at <time expression>", but it's optional
    match = re.search(r'\bat\b\s+(.+)', text)
    if match:
        time_str = match.group(1).strip()
        action = text[:match.start()].strip()
    else:
        # If 'at' isn't present, try parsing the last time-like expression
        words = text.split()
        for i in range(len(words)):
            dt = dateparser.parse(" ".join(words[i:]))
            if dt:
                time_str = " ".join(words[i:])
                action = " ".join(words[:i])
                break
        else:
            print("Could not parse the date/time.")
            return

    summary = action.strip().capitalize()
    dt = dateparser.parse(time_str)

    if not dt:
        print("Could not parse the date/time.")
        return

    start_time = dt.isoformat()
    end_time = (dt + timedelta(hours=1)).isoformat()

    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata',
        },
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {created_event.get('htmlLink')}")
    speak(f" {action} Event created sir !!")
    