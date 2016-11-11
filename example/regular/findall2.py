#!/usr/bin/python
# -*- coding:utf-8 -*- 

import   re
r=r"a[1]b"
print re.findall(r,"a1b")


#re.I实现忽略大小写
p_tel = re.compile(r,re.I)  
p_tel.findall('a1123a1b')

str = p_tel.findall('a1123a1B')
print  str
    

