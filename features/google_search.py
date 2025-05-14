from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re
import time
import sys 
sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak, listen

def get_search_result(command):
    key = re.search("search google for (.+)",command)

    # searching = command.split("for",1)[1] 
    # url = "https://google.co.in/search?q="
    if not key:
        speak("Didn't understood Sir, Please Repeat again!")
        return
    
    searching = key.group(1).strip()
    speak("Okay Sir!")
    speak(f"Searching for {searching}")
    service = Service(executable_path="./chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    # driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    url = "https://www.google.co.in/search?q=" + searching.replace(" ", "+")
    driver.get(url)
    time.sleep(10)