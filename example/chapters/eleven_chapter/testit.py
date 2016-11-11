#!/usr/bin/python
#!-*-conding:utf-8-*-

def testit(func,var1,*nkwargs,**kwargs):
    try:
        retval = func(var1,*nkwargs,**kwargs)
        result = (True,retval)
    except Exception, diag:
        result = (False,str(diag))
    else:
        pass
    finally:
        pass
    return result

def test():
    pass
    funcs = (int,long,float)
    vals = (1234,12.34,'1234','12.34')

    for eachFunc in funcs:
        print '_'* 20
        for eachVal in vals:
            retval = testit(eachFunc,eachVal)

            if retval[0]:
                print '%s(%s)= '% (eachFunc.__name__,'eachVal'),retval[1]
            else:
                print '%s(%s)= FAILED:'% (eachFunc.__name__,'eachVal'),retval[1]

if __name__=='__main__':
    test()