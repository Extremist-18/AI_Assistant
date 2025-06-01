import requests
import os 
import sys
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak, listen

from dotenv import load_dotenv
load_dotenv()

def get_weather(city_name="Surat"):
    API_KEY = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        speak("I'm sorry, I couldn't retrieve the weather information.")
        return

    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']

    speak(f"The weather in {city_name} is currently {weather}.")
    speak(f"The temperature is {temp} degrees Celsius, and it feels like {feels_like} degrees.")
    speak(f"The humidity level is {humidity} percent.")


def get_weather_text(city_name="Surat"):
    API_KEY = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to get weather data.")
        return

    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']

    text = f"Weather in {city_name}: {weather.capitalize()} \n Temperature: {temp}°C (Feels like {feels_like}°C) \n Humidity: {humidity}%"
    return text