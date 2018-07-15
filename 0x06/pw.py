#!/usr/bin/env python3
#
# pw.py - An insecure password locker program.
#
# just to try the complete syntax
from fakepyperclip import fakepyperclip as pyperclip
#
import logging
#
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s][%(module)s][%(name)s][%(levelname)-6s] - %(message)s",
	datefmt='%Y/%m/%d|%H:%M:%S'
    )
#
log=logging.getLogger("main")
#
log.debug("welcome to %s", __file__)
#

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

