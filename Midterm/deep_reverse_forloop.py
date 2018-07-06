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
        #l.reverse() reverse the list within
        size = len(l)
        templ = l.copy()
        for i in range(size):
            l[i] = templ[(size - 1) - i]
           

    
    #now reverse L in similar fashion
    
    sizeL = len(L)
    tempL = L.copy()
    for i in range(sizeL):
        L[i] = tempL[(size - 1) - i]
        
    
 
    


testL = [[1], [8, 4], [5, 6, 7], [2, 5, 7, 8]]

print(testL)

deep_reverse(testL)

print(testL)