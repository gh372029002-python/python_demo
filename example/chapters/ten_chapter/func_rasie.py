#!/usr/bin/python
# -*- coding:utf-8 -*- 
#文件名: raising.py raise实例

class ShortInputException(Exception):
	'''你定义的异常类。'''
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	s = raw_input('请输入 --> ')
	if len(s) < 3:
		raise ShortInputException(len(s), 3)
	# raise引发一个你定义的异常
except EOFError:
	print '/n你输入了一个结束标记EOF'
except ShortInputException, x:#x这个变量被绑定到了错误的实例
	print 'ShortInputException: 输入的长度是 %d,'\
        '长度至少应是 %d' % (x.length, x.atleast)
else:
	print '没有异常发生.'