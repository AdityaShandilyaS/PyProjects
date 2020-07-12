f = open("file.txt","rt")
#print(f.read())
s= f.read()
i=0
b=["0"]
b.clear()
for x in s:
	a=ord(x)
	"""if a<97:
		b.insert(i,chr(a))
	elif a == 122:
		b.insert(i,'b')
	elif a ==121:
		b.insert(i,'a')
	else:"""
	b.insert(i,chr(a+32))
	i+=1
f = open("decodedFile.txt","wt")
for x in b:
	f.write(x)