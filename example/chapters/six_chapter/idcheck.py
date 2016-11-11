#!/usr/bin/python
#!-*- coding:utf-8 -*-
"""
字符串标识符. 修改例6-1 的 idcheck.py 脚本,使之可以检测长度为一的标识符,并且可以识别 python 关键字.
   对后一个要求,你可以使用 keyword 模块(特别是 keyword.kwlist) 来辅助.
"""
import string,keyword

alphas = string.letters + '_'
nums = string.digits

print "Welcome to the Identifier Checker v1.0"
myInput = raw_input("Identifier to test? ")

if myInput in keyword.kwlist[:]:
    print """ invalid: is a keyword """
else:
    if myInput[0] not in alphas:
        print """ invalid: first symbol must be alphabetic """
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print """ invalid: remaining symbols must be alphanumeric """
                break
        else:
            print "okay as an identifier"