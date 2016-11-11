#!/usr/bin/python
# -*- coding:utf-8 -*-
# 异常try使用
"""
try:
    filename = raw_input('Enter file name: ');
    fobj = open(filename);

    for eachLine in fobj:
        print eachLine,
    fobj.close()
except IOError, e:
    print 'file open error:',e 
"""
try:
    assert 1 == 0, 'One does not equal zero silly!'
except AssertionError, args:
    print '%s: %s' % (args.__class__.__name__, args)