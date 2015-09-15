import random
import sys

nums = [random.randint(0, 1000000) for i in range(0, 10000)]
file = open('2.1/randints.txt', 'w')

for num in nums:
    file.writelines(str(num) + '\tNA\n')


def mapper:
    for line in sys.stdin:
        line = line.strip('\n')
        num, na = line.split(',')
        print '%s\t%s', num, 1


def reducer:
    for line in sys.stdin
        line = line.strip('\n')
        num, na = line.split(',')
        print '%s', num
