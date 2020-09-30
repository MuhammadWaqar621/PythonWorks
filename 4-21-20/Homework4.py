# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:57:20 2020

@author: waqar
"""

#a.
def any_lowercase1(s): 
    for c in s: 
        if c.islower(): 
            return True 
        else: 
            return False
#b.
def any_lowercase2(s): 
    for c in s: 
        if 'c'.islower(): 
            return 'True' 
        else: 
            return 'False'
#c.
def any_lowercase3(s): 
    for c in s: 
        flag = c.islower() 
    return flag
#d.
def any_lowercase4(s):
    flag = False 
    for c in s: 
        flag = flag or c.islower() 
    return flag
#e.
def any_lowercase5(s): 
    for c in s: 
        if not c.islower(): 
            return False 
        return True
