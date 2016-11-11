#!/usr/bin/python
# -*- coding:utf-8 -*-
# 提示用户输入文件名，然后打开一个文件，并显示他的内容到屏幕上。
filename = raw_input('Enter file name:');

fobj = open(filename,'r');

for eachLine in fobj:
    print eachLine
fobj.close()