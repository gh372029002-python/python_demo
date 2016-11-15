#!/usr/bin/python
#!-*-coding:utf-8-*-

class	HideX(object):
	def	__init__(self,x):
		self.x = x
	
	def 	get_x(self):
		return ~self.__x
	def	set_x(self,x):
		assert	isinstance(x,int),\
			'"x" must be an integer!'
		self.__x = ~x

	x = property(get_x,set_x)


inst = HideX(20)
print 'inst.x=',inst.x
inst.x =30
print 'inst.x=',inst.x


		
	
