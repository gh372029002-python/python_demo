#!/usr/bin/python
#!-*-conding:utf-8-*-

from random import randint
import sys

#ways 1
def odd(n):
    return n%2 #return 0 False or 1 True

allNums =[]
for eachNum in range(9):
    allNums.append(randint(1,99))
print filter(odd,allNums)

#ways 2
allNums =[]
for eachNum in range(9):
    allNums.append(randint(1,99))
print filter(lambda n : n%2,allNums)

#ways 3
allNums =[]
for eachNum in range(9):
    allNums.append(randint(1,99))
print [x for x in allNums if x%2]

#ways 4
print[x for x in [randint(1,99) for eachNum in range(9)] if x%2]
