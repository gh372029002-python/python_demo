#!/usr/bin/python
#!-*- coding:utf-8 -*-

queue =[]

def enQ():
    queue.append(raw_input('输入新的内容回车:').strip())

def deQ():
    if  len (queue)==0:
        print   'Cannot pop from an empty stack!'
    else:
        print   'Remoed[',`queue.pop(0)`,']'

def viewQ():
    print queue #calls  str() internally

CMDs    = {'e':enQ,'d':deQ,'v':viewQ}

def showmenu():
    pr =   """
    (E)nqueue
    (D)equeue
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
            if choice not in 'devq':
                print 'Invalid option,try again'
            else:
                break
        if  choice=='q':
            break
        CMDs[choice]()
if  __name__    ==  '__main__':
    showmenu()