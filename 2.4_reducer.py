#!/usr/bin/python
import sys
import math
import string

transtable = string.maketrans("","")

# input comes from STDIN (standard input)

# Placeholders for the vocabulary, frequencies
# Dictionary is of form {vocab_word: {0: x, 1:y}} where
# 0 and 1 are classes, and x and y are number of occurrences
# of vocab word in respective classes.
vocab = {}
class0_freq = 0
class1_freq = 0

# Read each line from standard in and keep adding
# class 0 and class 1 occurrences of the word into
# the dictionary.
for line in sys.stdin:
    words = line.strip('')
    words = line.split()
    if len(words) != 2:
        continue
    vocab.setdefault(words[0], {0: 0, 1:0})
    if int(words[1]):
        vocab[words[0]][1] += 1
    else:
        vocab[words[0]][0] += 1

# Class frequencies come in special keywords from the mapper.
# Extract them and remove them from the dictionary.
class_0_freq = vocab['class_0'][1]
class_1_freq = vocab['class_1'][1]
vocab.pop('class_0')
vocab.pop('class_1')

# Compute class probabilities
class_0_prob = class_0_freq * 1.0 / (class_0_freq + class_1_freq)
class_1_prob = class_1_freq * 1.0 / (class_0_freq + class_1_freq)

# Comput size of the vocabulary for each class from the compiled
# dictionary above.
class_0_vocab = 0
class_1_vocab = 0
for key in vocab:
    class_0_vocab += vocab[key][0]
    class_1_vocab += vocab[key][1]

# The probability math implemented below to predict class given a document.
# P(Spam | Document) > P(Not Spam | Document)
# => ln(P(Spam | Document) / P(Not Spam | Document)) > 0
# 
# So, we caclulate this value and the apply the above rule.
# ln(P(Spam | Document) / P(Not Spam | Document)) =
#   ln(P(Spam) / P(Not Spam)) + SUM(wi) {ln(P(word | Spam)/P(word | Not Spam))}

# P(Spam)/P(Not Spam) is always constant. Caclulate and store away.
ln_spam_not_spam = math.log(class_1_prob / class_0_prob)

# Read each document and compute the prediction using the algorithm above.
with open('enronemail_1h.txt') as infile:
    for document in infile:
        document = document.strip()
        document = document.split('\t')
        
        # If the document does not have subject/body fields, move on.
        if len(document) < 3 or len(document) > 4:
            continue
            
        # If it has the subject and body, catenate the two, otherwise use
        # the one available as the whole document.
        if len(document) == 4:
            content = document[2] + ' ' + document[3]
        else:
            content = document[2]
        
        # For each word in the document, compute the probability that the
        # word belongs to Spam/Not Spam classes.
        content = content.split()
        ln_word_spam_word_not_spam = 0
        for word in content:
            word = word.translate(transtable, string.punctuation)
            
            # If the word is in vocabulary, grab its frequency (plus one smoothing),
            # otherwise, just do plus one smoothing.
            if word in vocab:
                word_class_1_freq = vocab[word][1] + 1
                word_class_0_freq = vocab[word][0] + 1
            else:
                word_class_1_freq = 0 + 1
                word_class_0_freq = 0 + 1
            # Summation of the log ratios of word probabilities for each class.
            ln_word_spam_word_not_spam += math.log((word_class_1_freq * 1.0 /
                                                    (class_1_vocab + len(vocab))) /
                                                   (word_class_0_freq * 1.0 /
                                                    (class_0_vocab + len(vocab))))
        
        # The final caculation of the log odds ratio of class. If this ratio is
        # greater than zero, we have class 1, otherwise, class 0.
        ln_doc_spam_not_spam = ln_spam_not_spam + ln_word_spam_word_not_spam
        if ln_doc_spam_not_spam > 0:
            print '%s\t%s\t%s' % (document[0], document[1], 1)
        else:
            print '%s\t%s\t%s' % (document[0], document[1], 0)

