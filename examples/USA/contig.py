#!/usr/bin/env python

import fileinput

print "graph ContiguousStates {"

for line in fileinput.input():
	print "%s -- %s;" % tuple(line.split())

print "}"