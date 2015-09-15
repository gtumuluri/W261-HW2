#!/usr/bin/python
from operator import itemgetter
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    print words[0]