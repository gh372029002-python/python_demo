#!/usr/bin/python
# -*- coding:utf-8 -*-

"""偏函数"""
from operator import add,mul
from functools import partial
def mySum(x,y,z):return x+y+z
add1 = partial(add,1)
mul1 = partial(mul,100)
mysum1 = partial(mySum,2,100)

print add1(10)
print mul1(50)
print mysum1(50)