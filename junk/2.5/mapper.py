#!/usr/bin/python
import sys
import string

transtable = string.maketrans("","")

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if len(items) < 3:
        continue
    if items[1] != '0' and items[1] != '1':
        continue
    print '%s\t%s' % ('class_' + items[1], 1)    
    if len(items) == 3:
        content = items[2]
    if len(items) == 4:
        content = items[2] + ' ' + items[3]
    content = content.split()
    for word in content:
        word = word.translate(transtable, string.punctuation)
        # if word.find(sys.argv[1]) == 0:
        print '%s\t%s' % (word, items[1])