#!/usr/bin/python
#!--coding:utf8--
from random import choice

class RandSeq(object):
    def __init__(self,seq):
          self.data = seq

    def __iter__(self):
        return self
    
    def next(self):
        return choice(self.data)


for eachItem in RandSeq(('a','b','c')):
    print   eachItem