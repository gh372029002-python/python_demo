#!/usr/bin/python
#!-*- coding:utf-8 -*-

stack =[]

def pushit():
    stack.append(raw_input('输入新的内容回车:').strip())

def popit():
    if  len (stack)==0:
        print   'Cannot pop from an empty stack!'
    else:
        print   'Remoed[',`stack.pop()`,']'

def viewstack():
    print stack #calls  str() internally

CMDs    = {'u':pushit,'o':popit,'v':viewstack}

def showmenu():
    pr =   """
    P(U)sh
    P(O)P
    (V)iew
    (Q)uit
    Enter choice:"""

    while   True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except  (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'

            print '\nYou picked: [%s]' % choice
            if choice not in 'uovq':
                print 'Invalid option,try again'
            else:
                break
        if  choice=='q':
            break
        CMDs[choice]()
if  __name__    ==  '__main__':
    showmenu()