#!/usr/bin/env python3

"""	*fake pyperclip module*

pyperclip requires a clipboard mechanism such as X server, giving the following error:

Pyperclip could not find a copy/paste mechanism for your system.
For more information, please visit https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error

for the sake of the exercise this module simulates the behaviour via a texfile
"""
import logging

log=logging.getLogger("pyperclip")
#
def copy(clipboard):
	log.debug("copying %s", clipboard)
	
	try:
		with open("clipboard.txt", "w") as f:
			f.write(clipboard)
	except IOError:
		log.error("error saving clipboard to file")
	else:
		log.debug("%s copied succesfully", clipboard)

#
def paste():
	log.debug("copying %s", clipboard)

	try:
		with open("clipboard.txt", "r") as f:
			print(f.read())
	except IOError:
		log.error("error reading clipboard from file")
	else:
		log.debug("%s pasted succesfully", clipboard)
	
	
if __name__ == '__main__':
	log.warning("you shoul import this file")
