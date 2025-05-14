import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()
    
for i in range(10):
    try:
        with sr.Microphone(device_index=i) as source:
            print(f"\n Trying device {i}...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Speak now...")
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            print(f"Device {i} heard: {text}")
            break
    except Exception as e:
        print(f" Device {i} failed: {e}")

