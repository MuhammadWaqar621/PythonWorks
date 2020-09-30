# -*- coding: utf-8 -*-
"""

"""
import math 

def middle(llist):
    print ('Original List:')
    print (llist)
    llist.sort()
    print ('Sorted List:')
    print (llist)
    n=len(llist)
    if(n%2==0):
        print ('Median:')
        return sum(llist[(math.floor(n/2))-1:(math.floor(n/2))+1])/2
    else:
        print ('Median:')
        return llist[math.floor(n/2)]
print ('\nFor Odd Number of Element\n')
llist=[1,10,11,8,7,3, 4]
print(middle(llist))
print ('\nFor Even Number of Element\n')
llist=[1,10,11,8,7,3, 4,13]
print(middle(llist))
