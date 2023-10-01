import speech_recognition
from gtts import gTTS
import os

ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Hồn Quê: Mời bạn trò chuyện...")
    audio = ear.listen(mic)
try:
    text = ear.recognize_google(audio, language="vi-VI")
    print("Tôi: " + text)
except:
    text = "Tôi không hiểu những gì bạn nói"









