class two:
	time=0
	check = {0}
	name= "np"
	
def func(two):
	two.time += 10
	two.check.add(1)
	two.name ="asdfasdf"
	return two

c = two() 
c= func(c)
c.check.add(1)
c.check.add(3)
print(c.name, c.time, c.check)