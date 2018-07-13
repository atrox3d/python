#!/usr/bin/env python3
import sys
from pathlib import Path 

# just to try the complete syntax
from fakepyperclip import fakepyperclip as pyperclip

# log-like
print("[{}] first test".format(Path(sys.argv[0]).name))

#help(pyperclip)
print(pyperclip.__doc__)

pyperclip.copy("hello")
pyperclip.paste()

