#!/usr/bin/env python3
import sys
savestdout=sys.stdout

print("usage: %s 2>/dev/null" % sys.argv[0])

print("this is stdout")
sys.stdout = sys.stderr
print("is this stderr?")
stdoutid=id(sys.stdout)
stderrid=id(sys.stderr)
print("stdoutid: %s" % stderrid)
print("stderrid: %s" % stdoutid)
print("stdoutid == stderrid : %s" % (stdoutid == stderrid))

sys.stdout=savestdout
print("back to stdout")



