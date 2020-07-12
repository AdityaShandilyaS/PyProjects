import numpy as np

arraylist = []
unitx = [1, 0, 0]
unity = [0, 1, 0]
unitz = [0, 0, 1]

arraylist.append(unitx)
arraylist.append(unity)
arraylist.append(unitz)
print(arraylist)
arraylist = np.cross(arraylist, unitz)
print(arraylist)
