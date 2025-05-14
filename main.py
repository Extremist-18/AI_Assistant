# add music, take note, hide files and make them visible again
import speech_recognition as sr
import pyttsx3
import re
import time
from features.gmail_service import send_email, gmail_authenticate
from features.google_search import get_search_result
from features.search_person import search_wikipedia
from features.date_time import tell_date_time, tell_time, tell_date
from features.greet import greet
from features.yt_services import *
from features.news import *
from features.screenshot import take_screenshot

class AIAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.MIC_INDEX = 2
        self.emails = {
            "lalit": "lalitagrawal1808@gmail.com",
            "lalit college": "u21ec050@eced.svnit.ac.in"
        }

    def speak(self, text):
        try:
            voices = self.engine.getProperty('voices')
            self.engine.setProperty('voice', voices[0].id)
            self.engine.setProperty('rate', 175)
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            print("Sorry Sir, I didn't understand!")

    def listen(self):
        try:
            with sr.Microphone(device_index=self.MIC_INDEX) as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                self.recognizer.energy_threshold = 4000
                audio = self.recognizer.listen(source, timeout=5)
                print("Recognizing...")
                command = self.recognizer.recognize_google(audio, language='en-in').lower()
                print(f'You said: {command}')
                return command
        except Exception as e:
            print(f"Recognition error: {e}")
            return False

    def get_recipient(self, command):
        key = re.search("mail to (.+)", command)
        if not key:
            self.speak("Didn't understand Sir, please repeat again.")
            return None
        return key.group(1).strip()

    def handle_command(self, command):
        if "date" in command and "time" in command:
            tell_date_time()
        elif "date" in command:
            tell_date()
        elif "time" in command:
            tell_time()
        elif "stop" in command:
            self.speak("Goodbye Sir! Have a nice day ahead")
            return False
        elif "google" in command or "search" in command:
            get_search_result(command)
        elif "who is" in command:
            search_wikipedia(command)
        elif "play" in command or "play song" in command:
            # song = re.search("play (.+)",command)
            song = command.replace("play", "").replace("play song", "").strip()
            if not song:
                self.speak("Which song should i play sir?")
                song = listen()
            music_yt(song)    
        elif "news" in command or "headline" in command:
            match = re.search("tell me top (.+) headlines",command)
            x = int(match.group(1))
            speak_headlines(limit=x)
        elif "screenshot" in command:
            speak("What should be the file name?")
            name = self.listen() 
            cleaned = name.replace(" ", "")
            speak("Where should I save it?")
            path = self.listen()
            if not "desktop" in command
                take_screenshot(file_name=cleaned, location=path)
            else:
                take_screenshot(file_name = cleaned,location = None)    
        elif "send email" in command or "send an email" in command:
            recipient_key = self.get_recipient(command)
            if not recipient_key or recipient_key not in self.emails:
                self.speak("Recipient not found in my email book.")
                return True

            to_address = self.emails[recipient_key]
            self.speak(f"What should I include in the body of the email to {recipient_key}?")
            body = self.listen()
            self.speak("What should be the subject of the email?")
            subject = self.listen()
            send_email(gmail_authenticate(), to_address, subject, body)
            self.speak("Email has been sent.")
        else:
            self.speak(command)
        return True

    def run(self):
        # greet()
        while True:
            command = self.listen()
            if not command:
                self.speak("Please try again.")
                continue
            if not self.handle_command(command):
                break

if __name__ == "__main__":
    assistant = AIAssistant()
    assistant.run()
