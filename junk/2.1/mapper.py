#!/usr/bin/python
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    print '%s\t%s' % (words[0], 1)