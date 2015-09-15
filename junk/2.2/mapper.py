#!/usr/bin/python
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if len(items) == 4:
        words = items[3].split()
        for word in words:
            if word.find(sys.argv[1]) == 0:
                print '%s\t%s' % (word, 1)