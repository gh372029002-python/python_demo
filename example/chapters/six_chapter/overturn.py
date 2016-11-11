#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""myString  = raw_input('输入要翻转的字符串:')
strList =[]
for s in xrange(len(myString)):
    if myString[s].islower():
        myString = "%s%s%s" % (myString[:s],myString[s].upper(),myString[s+1:])
    elif myString[s].isupper():
        myString = "%s%s%s" % (myString[:s],myString[s].lower(),myString[s+1:])
    else:
        pass
print myString
"""

#使用swapcase实现
def myChang(myString):
    return myString.swapcase()

myString = raw_input("Enter a String: \n")
print myChang(myString)
