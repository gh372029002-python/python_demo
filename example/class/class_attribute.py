#!/usr/bin/python
# -*- coding: utf-8 -*-

class Employee(object):
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      '这是方法文档'
      print "Name : ", self.name,  ", Salary: ", self.salary

   if __name__ == '__main__':
      print '谁最到，我最大，我先执行'

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__ 
print Employee.displayEmployee.__doc__

Emp =  Employee('hello',20000)
Emp.displayEmployee()
