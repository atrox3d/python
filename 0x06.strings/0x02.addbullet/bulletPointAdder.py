#!/usr/bin/env python3
#
# BulletpointAdder.py - adds wikipedia bullet points to each line
#
import sys

sys.path.append("..") # Adds higher directory to python modules path
from lib.fakepyperclip import fakepyperclip as pyperclip

text = pyperclip.paste()

