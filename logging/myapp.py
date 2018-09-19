#!/usr/bin/env python3

# https://docs.python.org/3/howto/logging.html

import logging
import mylib

def main():
	logging.basicConfig(filename='myapp.log', level=logging.INFO)
	logging.info('start')
	mylib.dosomething()
	logging.info('end')

if __name__ == "__main__":
	main()

