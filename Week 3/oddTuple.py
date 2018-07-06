# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 10:25:17 2018

@author: sushy
"""

def oddTuple(aTup):
    odd = ()
    
    for i in range(len(aTup)):
        if i%2 == 0:
            odd = odd + (aTup[i],)
    
    return odd


print("Odd Tuple: " + str(oddTuple(('I', 'am', 'a', 'test', 'tuple'))))