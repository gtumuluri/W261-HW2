#!/usr/bin/python
import sys

# Simply read the standard input and output the value
# It comes in sorted order from the hadoop shuffle step
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    print words[0]