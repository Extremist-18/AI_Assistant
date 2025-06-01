from datetime import datetime
import sys
import pytz   
UTC = pytz.utc 
IST = pytz.timezone('Asia/Kolkata') 
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak, listen


def tell_date():
    x = datetime.now()
    x = x.strftime("%d %B %Y")
    return speak(x)

def tell_time():
    time_ist = datetime.now(IST) 
    x = time_ist.strftime("%I %M %p")
    return speak(x)

def tell_date_time():
    speak("Here's the current date and time.")
    x = datetime.now().strftime("%d %B %Y")
    speak(f"Today is {x}.")

    time_ist = datetime.now(IST).strftime("%I:%M %p")
    speak(f"The time now is {time_ist}.")
    