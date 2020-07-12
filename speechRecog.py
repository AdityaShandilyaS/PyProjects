import random
import speech_recognition as sr
from gtts import gTTS
import os
r = sr.Recognizer()
#mic = sr.Microphone()
har = sr.AudioFile('srTest2.wav')
with har as source:
	audio = r.record(source)
	text=r.recognize_google(audio)
	print(text)
	
"""with mic as source:
	audio = r.listen(source)
	text= r.recognize_google(audio)
	print(text)"""
greetings = ("hello", "hi", "greetings", "sup", "what's up", "best")
name = 'What is your name'
eat = 'What do you like to eat'
response = ["hi", "hey!", "hi there", "hello", "I am glad that you are talking to me"]

for word in text.split():
	if word in greetings:
		reply = random.choice(response)
		print(reply)
		myBot = gTTS(text=reply,lang='en',slow=False)
		myBot.save("greeting.wav")
	elif word in name:
		reply = 'My name is Venus'
		print(reply)
		myBot = gTTS(text=reply,lang='en',slow=False)
		myBot.save("name.wav")
	elif word in eat:
		reply = 'I like to eat raw data with some electricity'
		print(reply)
		myBot = gTTS(text=reply,lang='en',slow=False)
		myBot.save("food.wav")
	else:
		reply = 'Talk to me!'
		print(reply)
		myBot = gTTS(text=reply,lang='en',slow=False)
		myBot.save("Response.wav")
os.system("greeting.wav")
os.system("name.wav")
os.system("food.wav")
os.system("Response.wav")