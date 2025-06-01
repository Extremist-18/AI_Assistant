import requests
import os 
import sys
import datetime
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak, listen
sys.path.insert(0,'C:/Users/yasha/Desktop/Assistant/features')
from features.date_time import tell_date_time
from features.weather import get_weather

import pytz   
UTC = pytz.utc 
IST = pytz.timezone('Asia/Kolkata') 

def greet():
    hour = (int)(datetime.datetime.now(IST).strftime("%I"))

    if 5 <= hour < 12:
        greeting = "Good morning Sir!"
    elif 12 <= hour < 17:
        greeting = "Good afternoon Sir!"
    elif 17 <= hour < 23:
        greeting = "Good evening Sir!"
    else:
        greeting = "Hello! Hope you're having a calm night."

    speak(greeting)
    tell_date_time()
    speak("Let me also tell you the current weather.")
    get_weather()
