#!/usr/bin/python
import sys
import string

transtable = string.maketrans("","")

# Read input from the standard input
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    
    # If there is no content (as in subject/body in the data), skip
    if len(items) < 3:
        continue
    if items[1] != '0' and items[1] != '1':
        continue
    
    # Output a special word/keyword to allow reducer
    # to count the number of times a given class occurs.
    # Class is the second field in the data, so output
    # that by appending it to the 'class_' keyword string
    # and a count of 1 for each occurrence.
    print '%s\t%s' % ('class_' + items[1], 1)    
    if len(items) == 3:
        content = items[2]
    if len(items) == 4:
        content = items[2] + ' ' + items[3]
    content = content.split()
    
    # For each word in content, see if the word is same as user
    # chosen word, and then output the word and class to which
    # the document the word occurred in belongs to. This way, the
    # reducer can compute class frequencies for a given word.
    for word in content:
        # Remove punctuation
        word = word.translate(transtable, string.punctuation)
        if word.find(sys.argv[1]) == 0 or word.find(sys.argv[2]) == 0 or word.find(sys.argv[3]) == 0:
            print '%s\t%s' % (word, items[1])
