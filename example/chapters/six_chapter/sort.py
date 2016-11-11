#!/usr/bin/python
#!-*- coding:utf-8 -*-

#元组方式排序
aNumber =   raw_input("Please Enter a number,split with ','\n")
nuList = []
for anu in aNumber.split(",")[:]:
    nuList.append(int(anu))
nuList.sort(reverse=True)
print nuList


#字典方式排序
def sortDict(Dict):
    values = Dict.values()
    values.sort(reverse=True)
    print values

if  __name__    ==  "__main__":
    aDict = {'a':11,'c':43,'d':5,'ce':23}
    sortDict(aDict)