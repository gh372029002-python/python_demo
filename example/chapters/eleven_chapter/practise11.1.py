#!/usr/bin/python
#!-*-coding:utf-8-*-

"11章11.11练习题"
def countToFour1():
    for eachNum in range(5):
        print eachNum,
    pass

def countToFour2(n):
    for eachNum in range(n,9):
        print eachNum,
    pass

def countToFour3(n=1):
    for eachNum in range(n,9):
        print eachNum,
    pass

countToFour1()
print
countToFour2(0)
print
countToFour3(1)