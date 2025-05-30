
import os
import sys
import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Import your custom speak function
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
try:
    from util import speak
except ImportError:
    def speak(text): print("Assistant:", text)


def take_note(mic_index=None):
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    speak("Listening to your note, Sir!")

    try:
        with sr.Microphone(device_index=mic_index) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            recognizer.energy_threshold = 4000
            audio = recognizer.listen(source, timeout=10)

            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in').lower()
            print(f'You said: {command}')

            save_note(command)
            return command

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        speak("Could not request results from the speech recognition service.")
        return None
    except Exception as e:
        print(f"Recognition error: {e}")
        return None


def save_note(text):
    notes_dir = "notes"
    os.makedirs(notes_dir, exist_ok=True)

    filename = datetime.now().strftime("note_%Y%m%d_%H%M%S.txt")
    filepath = os.path.join(notes_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    speak(f"Your note has been saved as {filename}")


