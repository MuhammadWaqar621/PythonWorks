# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:25:19 2020

@author: waqar
"""

x = 0 
for i in range(3): 
    for j in range(3): 
        if i*j > 2: 
            x = x+3 
        elif i*j == 2: 
            x = x+2 
        else: 
            x = x-1 
    x = x-1 
print(x)
