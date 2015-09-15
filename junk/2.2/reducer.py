#!/usr/bin/python
import sys
# input comes from STDIN (standard input)
count = 0
for line in sys.stdin:
    if count == 0:
        words = line.strip()
        words = line.split()
    count += 1
print words[0], count