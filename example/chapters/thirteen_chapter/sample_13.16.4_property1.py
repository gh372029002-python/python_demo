#!/usr/bin/python
#!-*-coding:utf-8-*-

class	ProtectAndHideX(object):
	def	__init__(self,x):
		assert	isinstance(x,int),\
			'"x" must be an integer!'
		self.__x = ~x
	
	def 	get_x(self):
		return ~self.__x

	x = property(get_x)


#inst = ProtectAndHideX('foo')
inst = ProtectAndHideX(10)
print 'inst.x=',inst.x
inst.x =20
print 'inst.x=',inst.x


		
	
