import random
while True:
	class props:
		time =0
		check0 = {0} #6
		check1 = {0} #4

	def bedroom(props):
		while True:
			print(" ")
			a= input("A. Wear Formals  B. Wear Casuals  C. Wear sportswear  D. Exit ||")
			if a=='a' or a=='A' or a=='1':
				props.time += 10
				props.check0.add(1)
				print("10 mins spent")
				continue
			if a=='b' or a=='B' or a=='2':
				props.time += 5
				print("5 mins spent")
				continue
			if a=='c' or a=='C' or a=='3':
				props.time += 5
				props.check1.add(1)
				print("5 mins spent")
				continue
			if a=='d' or a=='D' or a=='4':
				props.time += 1
				print("A min spent")
				break
		return(props)
		
	def bathroom(props):
		while True:
			print(" ")
			a= input("A. Brush Teeth  B. Take a Bath  C. Apply Aftershave  D. Exit ||")
			if a=='a' or a=='A' or a=='1':
				props.time += 5
				props.check0.add(2)
				props.check1.add(2)
				print("5 mins spent")
				continue
			if a=='b' or a=='B' or a=='2':
				props.time += 10
				props.check0.add(3)
				print("10 mins spent")
				continue
			if a=='c' or a=='C' or a=='3':
				props.time += 5
				props.check0.add(4)
				print("5 mins spent")
				continue
			if a=='d' or a=='D' or a=='4':
				props.time += 1
				print("A min spent")
				break
		return(props)

	def hall(props):
		while True:
			print(" ")
			a= input("A. Have Cereal  B. Wear Formal Shoes  C. Have a Snackbar  D. Wear Sportshoes  E. Exit ||")
			if a=='a' or a=='A' or a=='1':
				props.time += 10
				props.check1.add(3)
				print("10 mins spent")
				continue
			if a=='b' or a=='B' or a=='2':
				props.time += 5
				props.check0.add(5)
				print("5 mins spent")
				continue
			if a=='c' or a=='C' or a=='3':
				props.time += 5
				props.check0.add(6)
				print("5 mins spent")
				continue
			if a=='d' or a=='D' or a=='4':
				props.time += 5
				props.check1.add(4)
				print("5 mins spent")
				continue		
			if a=='e' or a=='E' or a=='5':
				props.time += 1
				print("A min spent")
				break
		return(props)

	def corridor(props):
		while True:
			print(" ")
			a= input("Go to  A. The Bathroom  B. The Bedroom  C. The Hall  D. Office finally ||")
			if a=='a' or a=='A' or a=='1':
				props= bathroom(props)
				continue
			if a=='b' or a=='B' or a=='2':
				props= bedroom(props)
				continue
			if a=='c' or a=='C' or a=='3':
				props= hall(props)
				continue
			if a=='d' or a=='D' or a=='4':
				b= input("Are you sure? You won't be able to go back in y/n: ")
				if b=='y' or b=='Y':
					props.time += 15
				else:
					continue
				break
		return(props)

	t= props()
	n= input("Please select a scenario (enter 0 or 1): ")
	scenario = {
	0:"Oh Damn! It's 7.30! You woke up half an hour late! Get going! You need to be at office by 8.30, you have to meet a very sought after client, so make sure you are at your best, all the best! Remember, it takes 15mins to get to office",
	1:"Good morning! Time to get ready for the sports meet at office today, hope your tennis skills are warmed up. No important official work today, just be there quarter of an hour early so that you can give yourself time to warm-up before the match starts at 8.30. The time is 7.30 now, good luck!"
	}
	print("     LATE   FOR   WORK!!!     ")
	print(" ")
	print(scenario[int(n)])
	print(" ")
	t= corridor(t)
	if n=='0':
		if (60 - t.time) < 0 :
			print("Time Spent: ",t.time, " minutes")
			print("You were late for the meeting and hence lost the client. Learn from this mistake so as to never commit it again ")
		else:
			print("Time Spent: ",t.time, " minutes")
			flag = 1
			for x in range(7):
				if x in props.check0:
					continue
				else:
					if x ==1:
						print("Oops! always remember, important = formals. That actually works for when you're visiting your in-laws as well")
						flag = 0
						break
					elif x ==2:
						print("The client fainted when you greeted him! Guess you hadn't brushed your teeth. Please don't be giving him any CPR")
						flag = 0
						break
					elif x==3:
						print("The client was distracted by a foul odour coming from your side of the table. Should've listened to Mom about having a bath")
						flag = 0
						break
					elif x==4:
						print("the client shook your assistant's hand thinking he's in charge, what an embarrassing moment! Time to believe those aftershave ads after all")
						flag = 0
						break
					elif x==5:
						print("Did you just attend a meeting in your bare feet? Wow!")
						flag = 0
						break
					elif x==6:
						print("You're not a robot, should've eaten something, at least a snackbar. Now waste your client's precious time in the toilet farting all the gas away, disgrace!")
						flag = 0
						break
					else:
						print("all the best with your next task")
						flag = 0
						break
			
			if flag == 1:		
				print("You were on time! The clients were impressed with you. Congratulations! ")		
	if n=='1':
		if(45 - t.time) < 0 :
			print("Time Spent:",t.time, " minutes")
			print("Hard luck, you lost the match! Maybe you should've come earlier so that you could warm up thoroughly. Well, better luck next time")
		else:
			print("Time Spent:",t.time, " minutes")
			flag = 1
			for x in range(5):
				if x in props.check1:
					continue
				else:
					if x ==1:
						print("Wait, did you just enter a tennis court wearing formals? :|")
						flag = 0
						break
					elif x ==2:
						print("Your opponent fainted when you greeted him! And no, you didn't get a walkover, you're being charged with murder")
						flag = 0
						break
					elif x==3:
						print("C'mon! Sport ain't no Gym. Your 'diet' won't work here, eat substantially next time.")
						flag = 0
						break
					elif x==4:
						print("You're playing the finals, yet you forgot the most basic thing, no not your racquet, your shoes!")
						flag = 0
						break
					else:
						print("all the best with your next task")
						flag = 0
						break
			if flag == 1:			
				print("Congratulations! You won! That warm up surely helped huh...!")
