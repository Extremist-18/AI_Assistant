from datetime import datetime
import sys
import pytz   
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak, listen
sys.path.insert(0,'features')
from date_time import tell_date_time
UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata') 

def greet():
    time_ist = datetime.now(IST) 
    x = int(time_ist.strftime("%H"))

    if x<12:
        speak("Good Morning sir!")
    elif x>=12 and x<6:        
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    
    tell_date_time()  
    speak("Hope you are having a good day, How can i make it better sir? how can i help you today")
  