#!/usr/bin/python
import sys

# Initialize count, read lines from standard input
# and add up all words seen, print word and count
count = 0
for line in sys.stdin:
    if count == 0:
        words = line.strip()
        words = line.split()
    count += 1
print words[0], count