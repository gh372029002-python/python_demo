#!/usr/bin/python
#!-*-coding:utf-8-*-

j,k = 1,2

def proc1():
    j,k = 3,4
    print "j==%d and k==%d" % (j,k)
    pass

def proc2():
    j=6
    proc1()
    print "j==%d and k==%d" % (j,k)
    pass


k= 7
proc1()
print "j==%d and k==%d" % (j,k)

j = 8
proc2()
print "j==%d and k==%d" % (j,k)
