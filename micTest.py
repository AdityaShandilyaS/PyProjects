import random
import speech_recognition as sr
from gtts import gTTS
import os
r = sr.Recognizer()
mic = sr.Microphone()
#har = sr.AudioFile('srTest2.wav')
"""with har as source:
	audio = r.record(source)
	text= r.recognize_google(audio)
	print(text)"""
	
with mic as source:
	audio = r.listen(source)
	text= r.recognize_google(audio)
	print(text)