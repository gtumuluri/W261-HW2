#!/usr/bin/python
import sys
import math
import string

transtable = string.maketrans("","")

# input comes from STDIN (standard input)
vocab = {}
class0_freq = 0
class1_freq = 0

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

class_0_freq = vocab['class_0'][1]
class_1_freq = vocab['class_1'][1]
class_0_prob = class_0_freq * 1.0 / (class_0_freq + class_1_freq)
class_1_prob = class_1_freq * 1.0 / (class_0_freq + class_1_freq)
vocab.pop('class_0')
vocab.pop('class_1')

class_0_vocab = 0
class_1_vocab = 0
for key in vocab:
    class_0_vocab += vocab[key][0]
    class_1_vocab += vocab[key][1]

print class_0_freq, class_1_freq
print class_0_prob, class_1_prob
print class_0_vocab, class_1_vocab

# P(Spam | Document) > P(Not Spam | Document) => ln(P(Spam | Document) / P(Not Spam | Document)) > 0
# ln(P(Spam | Document) / P(Not Spam | Document)) = ln(P(Spam) / P(Not Spam)) + SUM(wi) {ln(P(word | Spam)/P(word | Not Spam))}

print class_0_vocab + class_0_freq, class_1_vocab + class_1_freq

ln_spam_not_spam = math.log(class_1_prob / class_0_prob)
with open('enronemail_1h.txt') as infile:
    for document in infile:
        document = document.strip()
        document = document.split('\t')
        if len(document) < 3 or len(document) > 4:
            continue
        if len(document) == 4:
            document = document[2] + ' ' + document[3]
        else:
            document = document[2]
        
        document = document.split()
        ln_word_spam_word_not_spam = 0
        for word in document:
            word = word.translate(transtable, string.punctuation)
            if word in vocab:
                word_class_1_freq = vocab[word][1] + 1
                word_class_0_freq = vocab[word][0] + 1
            else:
                word_class_1_freq = 0 + 1
                word_class_0_freq = 0 + 1
            ln_word_spam_word_not_spam += math.log((word_class_1_freq * 1.0 / (class_1_vocab + len(vocab))) /
                                                   (word_class_0_freq * 1.0 / (class_0_vocab + len(vocab))))
        
        ln_doc_spam_not_spam = ln_spam_not_spam + ln_word_spam_word_not_spam
        if ln_doc_spam_not_spam > 0:
            print 'SPAM'
        else:
            print 'NOT SPAM'

