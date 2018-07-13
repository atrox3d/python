#!/usr/bin/env python3

"""	*fake pyperclip module*

pyperclip requires a clipboard mechanism such as X server, giving the following error:

Pyperclip could not find a copy/paste mechanism for your system.
For more information, please visit https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error

for the sake of the exercise this module simulates the behaviour via a texfile
"""
def copy():
	print("copy")

def paste():
	print("paste")
	
if __name__ == '__main__':
	print("you shoul import this file")
