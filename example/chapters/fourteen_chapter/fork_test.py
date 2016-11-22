#!/usr/bin/python
#!-*-coding:utf-8-*-
import  os

ret = os.fork()
if ret==0:
    execvp('xbill',['xbill'])
else:
    os.wait()
