import speech_recognition as sr
import pyttsx3
import threading

r = sr.Recognizer()
engine = pyttsx3.init()

MIC_INDEX = 2  

def speak(text):
    try:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate',175)
        engine.say(text)
        engine.runAndWait()
    except:
        t = "Sorry Sir, I didn't Understood!"
        print(t)
  
def listen():
    try:
        r = sr.Recognizer()
        with sr.Microphone(device_index=MIC_INDEX) as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            r.energy_threshold = 4000
            audio = r.listen(source, timeout=5)
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in').lower()
            print(f'You said: {command}')
            return command
    except Exception as e:
        print(f"Recognition error: {e}")
        return False
