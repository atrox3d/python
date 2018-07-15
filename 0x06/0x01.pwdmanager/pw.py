#!/usr/bin/env python3
#
# pw.py - An insecure password locker program.
#
import sys
import logging
#
logging.basicConfig(
	level=logging.DEBUG,
	#format="[%(asctime)s][%(module)s][%(name)s][%(levelname)-6s] - %(message)s",
	format="%(asctime)s %(module)-15s %(levelname)-10s : %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
#
log=logging.getLogger(__name__)
#
# just to try the complete syntax
from fakepyperclip import fakepyperclip as pyperclip
#
log.debug("welcome to %s", __file__)
#
if len(sys.argv) <2:
	log.critical("Syntax: python %s account", sys.argv[0])
	sys.exit(1)

account = sys.argv[1]

PASSWORDS = {
				'email'		: 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
				'blog'		: 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
				'luggage'	: '12345'
			}

if account in PASSWORDS:
	if pyperclip.copy(PASSWORDS[account]):
		log.info( "password for %s copied to clipboard", account )
	else:
		log.fatal("something went wrong")
		sys.exit(2)
else:
	log.error("No account %s found", account)
	sys.exit(3)

