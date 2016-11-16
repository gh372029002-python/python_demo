#!/usr/bin/python
#!-*-coding:utf-8-*-

class   C(type):
    pass


class   CC(object):
    __metaclass__ = C

print type(C)
print type(CC)
