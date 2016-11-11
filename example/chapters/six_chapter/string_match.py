#!/usr/bin/python
#!-*- coding:utf-8 -*-


if __name__ == "__main__":
    aString = raw_input("Please Enter a String ...\n")
    for lNum in xrange(len(aString)):
        print "left %d Letter is %s, and right %d Letter is %s" % (lNum,aString[lNum],lNum,aString[::-1][lNum])

str = 'abcde';
for x in xrange(5):
    print str[::-1][x]