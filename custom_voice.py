import requests
import os
import tempfile
from playsound import playsound 

def tts_elevenlabs(text, voice_id, api_key):
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": api_key,
            # "Content-Type": "application/json"
        }
        data = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8
            }
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                f.write(response.content)
                audio_path = f.name

            playsound(audio_path)
            os.remove(audio_path)
        else:
            print("ElevenLabs API error:", response.text)

    except Exception as e:
        print("TTS error:", e)
