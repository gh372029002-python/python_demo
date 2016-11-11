#!/usr/bin/python
# -*- coding:utf-8 -*-

def mySum(x,y):return x+y
#way 1
allNums = range(9)
total = 0
for eachNum in allNums:
    total = mySum(total,eachNum)
print total
#way 2
total = reduce(mySum,allNums)
print total
