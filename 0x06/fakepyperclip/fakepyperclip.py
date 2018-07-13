#!/usr/bin/env python3

"""	*fake pyperclip module*

pyperclip requires a clipboard mechanism such as X server, giving the following error:

Pyperclip could not find a copy/paste mechanism for your system.
For more information, please visit https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error

for the sake of the exercise this module simulates the behaviour via a texfile
"""
def copy(clipboard):
	with open("clipboard.txt", "w") as f:
		f.write(clipboard)

def paste():
	with open("clipboard.txt", "r") as f:
		print(f.read())
	
	
if __name__ == '__main__':
	print("you shoul import this file")
