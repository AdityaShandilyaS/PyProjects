import speech_recognition as sr
from gtts import gTTS
import os
#from tempfile import TemporaryFile

class QuestionAnswerSet:
    number = 0
    question = ""
    answer = {""}


def testLoop(QuestionAnswerSet):
    # print("inside testLoop main")
    parser = {""}

    recite = QuestionAnswerSet.question
    print(recite)
    myBot = gTTS(text=recite, lang='en-GB', slow=False)
    myBot.save("question.wav")
    os.system("question.wav")
    """f = TemporaryFile()
    myBot.write_to_fp(f)
    f.close()"""

    # print(qaSet.a)

    r = sr.Recognizer()
    mic = sr.Microphone()
    #har = sr.AudioFile('engTrainer.wav')
    with mic as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        print(text)

    for word in text.split():
        parser.add(word.lower())
    print(parser)
    print(QuestionAnswerSet.answer)
    diff = (QuestionAnswerSet.answer - parser)
    print(len(diff))

    if len(diff) is 0:
        reply = 'correct!'
        print(reply)
        myBot = gTTS(text=reply, lang='en-GB', slow=False)
        myBot.save("result.wav")
        os.system("result.wav")
        """fi = TemporaryFile()
        myBot.write_to_fp(fi)
        fi.close()"""
        flag = 1
    # break
    else:
        reply = 'Wrong answer, try again'
        print(reply)
        myBot = gTTS(text=reply, lang='en-GB', slow=False)
        #myBot.save("result.wav")
        #os.system("result.wav")
        fi = TemporaryFile()
        myBot.write_to_fp(fi)
        fi.close()
        flag = 0
    # break
    return flag


question1 = QuestionAnswerSet()
question1.number = 1
question1.question = "Introduce yourself as James from Swiggy"
question1.answer = {"james", "swiggy"}

question2 = QuestionAnswerSet()
question2.number = 2
question2.question = "Confirm the order which consists of a burger, fries and a drink"
question2.answer = {"burger", "fries", "drink"}

# print(q2.q)

register = {
    1: question1,
    2: question2
}

x = int(1)

# print(len(register))
# print(value.register[2])

while x <= len(register):
    inp = input("press 1 to continue; 0 to quit")
    # print(inp)
    if inp == '1':
        # print("inside inp ifloop" +inp)
        flag = testLoop(register[x])
        if flag == 1:
            x = x + 1
    elif inp == '0':
        exit(0)


