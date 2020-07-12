import random
while True:
	inp= input("Guess the number on the dice "+"("+"0 to exit"+") ")
	n= random.choice([1,2,3,4,5,6])
	if inp == '0':
		break;
	if (n == int(inp)):
		print("Right guess! Rolled number: ", n)
	else:
		print("Try again! Rolled number: ", n)
