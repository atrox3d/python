#!/usr/bin/env python3

class Reverse:
	"""
	Creates backwards-loop Iterators
	"""
	def __init__(self, data):
		self.data=data
		self.index=len(data)
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index -= 1
		return self.data[self.index]
		

lst=[34,978,42]

backlist = Reverse(lst)
for el in backlist:
	print(el)

	