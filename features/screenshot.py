import pyautogui
import os
from datetime import datetime
import sys
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak

def take_screenshot(file_name=None, location=None):
    try:
        if not file_name:
            file_name = datetime.now().strftime("screenshot_%Y%m%d_%H%M%S")
        if not file_name.endswith(".png"):
            file_name += ".png"

        # Use Desktop if location not provided
        if not location:
            location = os.path.join(os.path.expanduser("~"), "Desktop")
        os.makedirs(location, exist_ok=True) 

        full_path = os.path.join(location, file_name)
        screenshot = pyautogui.screenshot()
        screenshot.save(full_path)
        speak(f"Screenshot saved as {file_name} at Desktop")
        print(f"[INFO] Screenshot saved at {full_path}")

    except Exception as e:
        speak("Sorry, I couldn't take the screenshot.")
        print(f"[ERROR] {e}")
