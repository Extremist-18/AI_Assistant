import requests
import os
from dotenv import load_dotenv
load_dotenv()
import sys
sys.path.insert(0,'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak

def fetch_toi_headlines(limit):
    api_key = os.getenv("NEWS_API")
    if not api_key:
        raise ValueError("API key not found. Please check your .env file.")

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"sources=bbc-news&language=en&pageSize={limit}&apiKey={api_key}"
    )
    
    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        raise Exception("Failed to fetch news. Check API or URL.")

    return [article["title"] for article in data["articles"][:limit]]


def speak_headlines(limit):
    headlines = fetch_toi_headlines(limit=limit)
    print(headlines)
    speak(f"Here are the top {limit} headlines from Times of India.")
    x = 1
    for headline in headlines:
        speak(str(x))
        speak(headline)
        x+=1
    
    