#!/usr/bin/python
#!-*-coding:utf-8-*-
import  os

ret = os.fork()
if ret==0:
    execvp('ls')
else:
    os.wait()
