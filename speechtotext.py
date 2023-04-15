import speech_recognition
from gtts import gTTS
import os

ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Hon Que: I'm listening to you...")
    audio = ear.listen(mic)
try:
    text = ear.recognize_google(audio, language="vi-VI")
    print("You: " + text)
except:
    text = "I don't understand what you're talking about."








