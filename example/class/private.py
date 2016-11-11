#!/usr/bin/python 
# -*- coding:utf-8 -*- 

class JustCounter:
    __secretCount = 0; # 私有属性
    publicCount =  0;  # 公共属性

    def count(self):
        self.__secretCount +=1
        self.publicCount +=1
        print self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount

# print counter.__secretCount  # 报错，实例不能访问私有变量
print counter._JustCounter__secretCount #Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性，将如下代码替换以上代码的最后一行代码