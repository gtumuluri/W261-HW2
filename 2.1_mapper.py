#!/usr/bin/python
import sys

# Simply read the input from standard inpit and output
# the number and the count (1) - the latter does not matter.
for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    print '%s\t%s' % (words[0], 1)