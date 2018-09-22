#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging

#from lib import lib1
import lib.lib1 as lib1
# the default level is warning so only the first line will be printed
logging.basicConfig(level=logging.INFO)
logging.info('this is %s logging', __name__)
lib1.hello()

