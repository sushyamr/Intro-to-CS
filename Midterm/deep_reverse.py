# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 06:31:24 2018

@author: sushy
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    
    for l in L:
        l.reverse()
        
    
    L.reverse()
    


testL = [[1], [8, 4], [5, 6, 7], [2, 5, 7, 8]]

print(testL)

deep_reverse(testL)

print(testL)