#!/usr/bin/env python3
import sound

print("sound           : %s" % sound)

try:
	print("sound.effects   : %s" % sound.effects)
except Exception as e:
	print("error           : %s" % e)


