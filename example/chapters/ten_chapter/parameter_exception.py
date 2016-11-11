#!/usr/bin/python
#!-*-coding:utf-8-*-

var = raw_input('Enter object:')
try:
    retval = float(var)
except (ValueError,TypeError),diag:
    retval = str(diag)

print retval
