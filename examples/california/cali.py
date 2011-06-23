#!/usr/bin/env python

import fileinput

print "graph People {"

for line in fileinput.input():
	stuff = line.replace(".", "").split()
	print "%s;" % "--".join(stuff)
print "}"