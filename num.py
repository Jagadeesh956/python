import numpy as np
from learntools.python import jimmy_slots
# rolls = np.random.randint(low=1, high=6, size=10)
# print(rolls)
#
# print(rolls<3)
xlist = [[1,2,3],[2,4,6],[3,4,6]]
x = np.array(xlist)
print("xlist ={}".format( x))
#get the last element in second row of the 2D array
print(x[1,-1])
# Get the last element of the second sublist of our nested list?
print(xlist[1][-1])

help(jimmy_slots)