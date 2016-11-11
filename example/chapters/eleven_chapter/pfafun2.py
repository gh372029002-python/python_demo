#!/usr/bin/python
# -*- coding:utf-8 -*-

"""偏函数"""
from operator import add,mul
from functools import partial

baseTwo = partial(int,base=2)
baseTwo.__doc__ = 'Convent base 2..'
print baseTwo('10010')