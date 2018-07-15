#!/usr/bin/env python3

"""	*fake pyperclip module*

pyperclip requires a clipboard mechanism such as X server, giving the following error:

Pyperclip could not find a copy/paste mechanism for your system.
For more information, please visit https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error

for the sake of the exercise this module simulates the behaviour via a texfile
"""
import logging

log=logging.getLogger(__name__)
#
def copy(clipboard):
	log.debug("copying %s", clipboard)
	
	try:
		with open("clipboard.txt", "w") as f:
			f.write(clipboard)
	except IOError as e:
		log.fatal("error saving clipboard to file: %s", e)
		return False
	else:
		log.debug("%s copied succesfully", clipboard)
		return True

#
def paste():
	log.debug("copying %s", clipboard)

	try:
		with open("clipboard.txt", "r") as f:
			print(f.read())
	except IOError as e:
		log.fatal("error reading clipboard from file: %s", e)
		return False
	else:
		log.debug("%s pasted succesfully", clipboard)
		return True


if __name__ == '__main__':
	log.warning("you should import this file")
