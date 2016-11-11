#!/usr/bin/python
#!-*-coding:utf-8-*-
from random import randint

"""Éú³ÉÆ÷-randGen"""

def randGen(aList):
    while len(aList)>0:
        yield aList.pop(randint(0,len(aList)-1))
        print len(aList)
        
for item  in randGen(['rock', 'paper', 'scissors']):
    print item

