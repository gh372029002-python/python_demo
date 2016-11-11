#!/usr/bin/python
#!--coding:utf8--

class AnyIter(object):
    """docstring for ClassName"""
    def __init__(self,data, safe = False):
        self.safe   =   safe
        self.iter = iter(data)
    def __iter__(self):
        return self
        pass
    def next(self,howmany=1):
        retval = []
        for eachItem in xrange(howmany):
            try:
                retval.append(self.iter.next())
            except Exception, e:
                if self.safe:
                    break
                else:
                    raise
        return retval

a = AnyIter(range(10),True)
i = iter(a) 

for j in xrange(1,5):
    print j,":",i.next(j)    
    pass  
#AnyIter安全锁
i = iter(a) 
i.next(11)   