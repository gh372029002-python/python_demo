#!/usr/bin/python
#!--coding:utf-8--
class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj
    def get(self):
        return self.__data
    def __repr__(self):
        return 'self.__data'
    def __str__(self):
        return str(self.__data)
    def __getattr__(self, attr):
        return getattr(self.__data, attr)

wrappedList = WrapMe([123, 'foo', 45.67])
wrappedList.append('陈')
wrappedList.append('ER')
wrappedList.append('狗')
print wrappedList.get()[3]