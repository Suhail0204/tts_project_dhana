# tts_file.py

import requests

def ttsmodel(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/P7x743VjyZEOihNNygQ9"

    payload = {
        "model_id": "eleven_monolingual_v1",
        "text": text,
    }

    headers = {
        "xi-api-key": "bf62844eda451ebbb8a74429dfae5c6b",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        audio_content = response.content
        with open("static/output2.mp3", "wb") as f:
            f.write(audio_content)
        print("Audio saved to output2.mp3")
    else:
        print(f"Error: {response.status_code} - {response.text}")

ttsmodel("This is the sample")