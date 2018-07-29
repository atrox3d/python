#!/usr/bin/env python3
import sys, os

os.environ['YO']="1" # won't alter parent shell

print("export YO=1") # eval $(env.py)

