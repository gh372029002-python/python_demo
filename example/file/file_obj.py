#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# 打开一个文件
fo = open("foo.txt", "wb")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace

print '\n'
# 打开一个文件
fo = open("foo.txt", "wb")
print "文件名: ", fo.name
 
# 关闭打开的文件
fo.close()

#在这里，被传递的参数是要写入到已打开文件的内容.
# 打开一个文件
fo = open('foo.txt', 'wb')
fo.write( "www.runoob.com!\nVery good site!\n");

fo = open('foo.txt','r');
print "访问模式 : ", fo.mode
# 关闭打开的文件
for eachLine    in  fo:
    print   eachLine,
fo.close()
