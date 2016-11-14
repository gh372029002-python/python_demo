#!/usr/bin/python
#!-*-coding:utf-8-*-

from    time    import  time,ctime,sleep
class TimeWrapMe(object):
    """docstring for TimeWrapMe"""
    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = \
        self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self,t_type):
        if not isinstance(t_type,str) or t_type[0] not in 'cma':
            raise   TypeError,\
                    "argument   of  'c','m', or 'a' req'd"
        # print getattr(self,'_TimeWrapMe__ctime')
        return  getattr(self,'_%s__%stime' %\
                    (self.__class__.__name__, t_type[0]))
        pass

    def gettimestr(self,t_type):
        return  ctime(self.gettimeval(t_type))
        pass

    def set(self,obj):
        self.__data = obj
        self.__mtime = self.__atiime = time()
        pass

    def __repr__(self): #repr()
        self.__atime = time()
        return 'self.__data'
    def __str__(self): #str()
        self.__atime = time()
        return str(self.__data)
        pass

    def __getattr__(self,attr): #delegae
        self.__atime = time()
        return getattr(self.__data,attr)
        pass

timeWrappedObj  =   TimeWrapMe(932)
sleep(2)
# print timeWrappedObj.gettimestr('c')+'\n'
# print timeWrappedObj.gettimestr('m')+'\n'
# print timeWrappedObj.gettimestr('a')+'\n'
print timeWrappedObj
print timeWrappedObj.gettimestr('c')+'\n'
print timeWrappedObj.gettimestr('m')+'\n'
#延时2秒访问
print timeWrappedObj.gettimestr('a')+'\n'
print 'modify'
timeWrappedObj.set('time is up')
print timeWrappedObj.gettimestr('m')+'\n'
print timeWrappedObj.gettimestr('c')+'\n'
print timeWrappedObj.gettimestr('m')+'\n'
print timeWrappedObj.gettimestr('a')+'\n'
