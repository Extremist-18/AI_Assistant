from datetime import datetime
import sys
import pytz   
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak, listen
sys.path.insert(0,'features')
from date_time import tell_date_time
UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata') 
import requests

def get_weather(city_name="Surat"):
    API_KEY = "bf67c19357c9ab0b7ce34207ec29b598"
    API_KEY = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        print("⚠️ Failed to get weather data.")
        return

    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']

    speak(f"🌤️ Weather in {city_name}: {weather.capitalize()}")
    speak(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
    speak(f"💧 Humidity: {humidity}%")


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
    get_weather()
    speak("Hope you are having a good day, How can i make it better sir? how can i help you today")
  