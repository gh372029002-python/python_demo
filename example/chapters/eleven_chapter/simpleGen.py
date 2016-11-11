#!/usr/bin/python
#!-*-coding:utf-8-*-

"""Éú³ÉÆ÷-simple1"""

def simpleGen():
    yield 1
    yield '2-->punch!'
 
myG =   simpleGen()
print myG.next()

print myG.next()

try:
    print myG.next()
except StopIteration,si:
    print si
    print 'str(StopIteration):\t', str(StopIteration)
    print 'str(e):\t\t', str(si)
    print 'repr(e):\t', repr(si)

for eachItem  in simpleGen():
    print eachItem
    pass
    
    
