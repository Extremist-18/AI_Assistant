import webbrowser
import re
import time
import sys 
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak, listen

def get_search_result(command):
    key = re.search("search google for (.+)", command)
    if not key:
        speak("Didn't understood, please try again")
        return
    
    searching = key.group(1).strip()
    speak("Okay Sir!")
    speak(f"Searching for {searching}")
    
    url = "https://www.google.co.in/search?q=" + searching.replace(" ", "+")
    
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
    webbrowser.get('brave').open_new_tab(url)

    time.sleep(10)
