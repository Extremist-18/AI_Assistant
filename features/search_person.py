import wikipediaapi
import webbrowser
import re 
import sys 
import time
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak, listen

def search_person(person):
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='JarvisAssistant/1.0 (u21ec050@eced.svnit.ac.in)'
    )

    search_title = person.title()  # "Apj Abdul Kalam"
    page = wiki.page(search_title)

    if not page.exists():
        return "Page not found."

    webbrowser.open(page.fullurl)
    return page.summary[:500]
    
def search_wikipedia(command):
    key = re.search("who is (.+)",command)
    if not key:
        speak("Didn't understood Sir, Please Repeat again!")
        return
    
    searching = key.group(1).strip()
    speak(f"Searching for {searching}")
    search_person(searching)
    time.sleep(10)
