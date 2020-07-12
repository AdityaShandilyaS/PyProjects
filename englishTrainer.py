import speech_recognition as sr
from gtts import gTTS
import os

class questionanswerSet:
	number = 0
	question = ""
	answer = {""}

def testLoop(qaSet):
	#print("inside testLoop main")
	parser = {""}
	
	recite = qaSet.q
	print(recite)
	myBot = gTTS(text=recite,lang='en-GB',slow=False)
	myBot.save("question.wav")
	os.system("question.wav")
	
	#print(qaSet.a)
	
	r = sr.Recognizer()
	#mic = sr.Microphone()
	har = sr.AudioFile('engTrainer.wav')
	with har as source:
		audio = r.record(source)
		text=r.recognize_google(audio)
		print(text)
	
	for word in text.split():
		parser.add(word.lower())
	print(parser)
	print(qaSet.a)
	diff = (qaSet.a - parser)
	print(len(diff))
	
	if len(diff) is 0:
		reply = 'correct!'
		print(reply)
		myBot = gTTS(text=reply,lang='en-GB',slow=False)
		myBot.save("result.wav")
		os.system("result.wav")
		flag = 1
		#break
	else:
		reply = 'Wrong answer, try again'
		print(reply)
		myBot = gTTS(text=reply,lang='en-GB',slow=False)
		myBot.save("result.wav")
		os.system("result.wav")
		flag = 0
		#break
	return flag

q1 = qaSet()
q1.n = 1
q1.q = "Introduce yourself as James from Swiggy"
q1.a = {"james", "swiggy"}

q2 = qaSet()
q2.n = 2
q2.q = "Confirm the order which consists of a burger, fries and a drink"
q2.a = {"burger", "fries", "drink"}

#print(q2.q)

register = {
	1: q1,
	2: q2
}

x = int(1) 

#print(len(register))
#print(value.register[2])

while x <= len(register):
	inp = input("press 1 to continue; 0 to quit")
	#print(inp)
	if inp == '1':
		#print("inside inp ifloop" +inp)
		f = testLoop(register[x])
		if f == 1:
			x = x + 1
	elif inp == '0':
		exit(0)


