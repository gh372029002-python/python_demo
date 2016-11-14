#!/usr/bin/python
#!-*-coding:utf-8-*-
class CapOpen(object):
    """docstring for CapOpen"""
    def __init__(self, fn,mode='r',buf=-1):
        self.file = open(fn,mode,buf)

    def __str__(self):
        return  str(self.file)

    def __repr__(self):
        return 'self.file'

    def write(self,line):
        self.file.write(line.upper())
    
    def __getattr__(self,attr):
        return  getattr(self.file,attr)

path = './tmp.text'

f = CapOpen(path,'w')

f.write('hello')  
f.write('word')  
f.write('!')  
f.close()
 

f = CapOpen(path,'r')

# for eachLine in f.file:
for eachLine in f:
    print eachLine,

# f = open(path,'r',-1)
# for eachLine in f:
    # print eachLine,
