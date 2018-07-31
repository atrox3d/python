#!/usr/bin/env python3
#
#	https://www.python-course.eu/python3_deep_copy.php
#
x=3
y=x
print(id(x), id(y))
print(x,y)

y=4
print(id(x), id(y))
print(x,y)

def printcolors():
	print("colours1     : %s" % colours1)
	print("colours2     : %s" % colours2)
	print("id(colours1) : %s" % id(colours1))
	print("id(colours2) : %s" % id(colours2))
	print("same id      : %s" % (id(colours1) == id(colours2)))
	print()

def printlists():
	print("list1     : %s" % list1)
	print("list2     : %s" % list2)
	print()

colours1 = ['red', "blue"]
colours2 = colours1
printcolors()

colours2 = ["rouge", "vert"]
printcolors()

#
colours2 = colours1
printcolors()

colours2[1] = "green"
printcolors()

print ("------------------------------------------------------------------------")

list1 = ['a','b','c','d']
list2 = list1[:]
list2[1] = 'x'
printlists()
