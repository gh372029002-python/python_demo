#!/usr/bin/python

from    random  import  randint, choice
from    string  import  lowercase
import    sys
from    sys     import  maxint
from    time    import  ctime

doms = ('com','edu','net','org','gov')
f = open('gendatatmp.txt','a+')

for i in range(randint(5,10)):
    dtint   = randint(0,maxint-1)
    print dtint
    dtstr   = ctime(dtint/1000)
    shorter = randint(4,7) 
    
    em = ''
    for j in range(shorter):
        em += choice(lowercase)

    longer = randint(shorter,12)
    dn = ''
    for j in range(longer):
        dn +=choice(lowercase)

    word =  '%s::%s@%s.%s::%d-%d-%d\n' % (dtstr,em,dn,choice(doms),dtint,shorter,longer)
    print word,
    f.write(word)
    
f.close()