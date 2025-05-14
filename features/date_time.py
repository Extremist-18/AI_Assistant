from datetime import datetime
import sys
import pytz   
UTC = pytz.utc 
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak, listen

IST = pytz.timezone('Asia/Kolkata') 

def tell_date():
    x = datetime.now()
    x = x.strftime("%d %B %Y")
    return speak(x)

def tell_time():
    time_ist = datetime.now(IST) 
    x = time_ist.strftime("%I %M %p")
    return speak(x)

def tell_date_time():
    speak("Todays date is ")
    tell_date()
    speak("And current time is ")
    tell_time()