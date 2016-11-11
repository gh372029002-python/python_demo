#!/usr/bin/python
#!-*- coding:utf-8 -*-

gradList= []
listSum = 0

while True:
    aScore  = raw_input("Please Enter your point:\n")
    if aScore == '-1':
        break
    gradList.append(float(aScore))
    listSum+=float(aScore)

print "the average Score is %.2f" % (listSum/len(gradList))



