#!/usr/bin/env python3
import os, sys
import logging
import shelve
#
#	logger configuration
#
logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s %(module)-15s %(levelname)-10s : %(message)s",
	datefmt='%Y/%m/%d %H:%M:%S'
	)
#
#	get a logger
#
log=logging.getLogger(__name__) 
#
#	using literal string interpolation (f-strings) to create variable width format
#
width=20
formats=f'%-{width}.{width}s : %s'
formatd=f'%-{width}.{width}s : %d'

def writeshelf(shelf):
	shelf['string'] = "hello there"
	shelf['tuple'] = (1,2,3)
	shelf['list'] = [1,2,3]
	shelf['dict'] = { 'one' : 1, 'two' : 2}


shelf=shelve.open('shelf')

if len(shelf.items()) == 0:
	writeshelf(shelf)

log.info(formatd, 'shelf item count', len(shelf.items()) )

for item in shelf.items():
	log.info(formats,	'item', item)

for key in shelf.keys():
	log.info(formats,	'key', key)

for value in shelf.values():
	log.info(formats,	'value', value)

