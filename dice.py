import random
while True:
	arg= input("Press y to roll the dice; n to exit: ")
	if arg == 'y':
		print(random.choice([1,2,3,4,5,6]))
	elif arg == 'n':
		break;