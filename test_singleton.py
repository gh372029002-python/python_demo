#!/usr/bin python 
#-*- coding:utf-8 -*-
class Singleton(object):
 
  def __new__(cls, *args, **kwargs):
    if not hasattr(cls, '_instance'):
      orig = super(Singleton, cls)
      cls._instance = orig.__new__(cls, *args, **kwargs)
    return cls._instance
 
class MyClass(Singleton):
  a = 1
 
one = MyClass()
two = MyClass()
print id(one)  # 29097904
print id(two)  # 29097904
print one == two  # True
print one is two  # True
print one is two  # True
