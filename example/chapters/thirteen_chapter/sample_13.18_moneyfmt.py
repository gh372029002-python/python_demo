#!/usr/bin/python
#!-*-coding:utf-8-*-

class MoneyFmt(object):
    def __init__(self, value = 0.0):    # constructor
        self.value = float(value)
        
    def update(self, value = None):     # allow updates
        ### (a) Begins
        if value != None:
            self.value = float(value)
            print 'Value has been updated, the new value is: ', self.value
        else:
            print 'Value has not been updated.'
        ### (a) Ends
    
    def __repr__(self):                 # display as a float
        return repr(self.value)
    
    def __str__(self):                  # formatted display
        val = ''
        ### (b) Begins
        roundi = round(self.value, 2)
        absi = abs(roundi)
        if (absi * 10) % 1 == 0:
            value = format(absi, ',') + '0'
        else:
            value = format(absi, ',')
        
        if roundi >= 0:
            val = '$' + value
        else:
            val = '-' + '$' + value
        ### (b) Ends
        
        return val
    
    def __nonzero__(self):              # boolean test
        ###
        ### (c) find and fix the bug
        ###
        return int(self.value) 
    
cash = MoneyFmt(123.456)
cash
print cash
cash.update(100000.4567)
cash
print cash
cash.update(-0.3)
cash
print cash
repr(cash)
print `cash`
print str(cash)