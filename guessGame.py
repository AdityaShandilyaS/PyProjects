import random
import RPi.GPIO as gpio

led1 = 40
led2 = 33
buzz = 29
gpio.setmode(gpio.BOARD)
gpio.setup(led1, gpio.OUT, initial = 0)
gpio.setup(led2, gpio.OUT, initial = 0)
gpio.setup(buzz, gpio.OUT, initial = 0)
while True:
	inp= input("Guess the number on the dice "+"("+"0 to exit"+") ")
	gpio.output(buzz, False)
	n= random.choice([1,2,3,4,5,6])
	if inp == '0':
		gpio.output(buzz, False)
		gpio.output(led1, False)
		gpio.output(led2, False)
		break;
	if (n == int(inp)):
		gpio.output(led1, False)
		gpio.output(led2, True)
		gpio.output(buzz, True)
		print("Right guess! Rolled number: ", n)
	else:
		gpio.output(led1, True)
		gpio.output(led2, False)
		gpio.output(buzz, True)
		print("Try again! Rolled number: ", n)
gpio.cleanup()
		
