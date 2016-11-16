#!/usr/bin/python
#!-*-coding:utf-8-*-

class SlottedClass(object):
    """docstring for SlottedClass"""
    # __slots__ = ('foo','bar','__dict__')
    bar ='1'
c = SlottedClass()
print c
#带__slots__属性的类定义不会存在__dict__了
try:
    print c.__dict__
except AttributeError, e:
    print e.__repr__

# print c.__dict__
c.foo = 'foooo'
print c.foo
c.__dict__= {'1':1}
print c.__dict__
c.foo = 1
print SlottedClass.__dict__
print type(c).__dict__['bar'].__get__(c, type(c))
print SlottedClass.__dict__['bar'].__get__(None, SlottedClass)