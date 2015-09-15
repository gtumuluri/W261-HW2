#!/usr/bin/python

import sys

# Take input from the standard input
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    # Look for the 'body' portion of the email message
    if len(items) == 4:
        words = items[3].split()
        for word in words:
            # If the word in the body matches user specified,
            # output its occurrence
            if word.find(sys.argv[1]) == 0:
                print '%s\t%s' % (word, 1)