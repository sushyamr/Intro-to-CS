# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 12:00:11 2018

@author: sushy
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    guess = len(aStr)//2
    
    
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr
    if char < aStr[guess]:
        return isIn(char, aStr[:guess])
    elif char == aStr[guess]:
        return True
    else:
        return isIn(char, aStr[guess:])
        
    
    


print(isIn('x', 'abcdefxyz'))
print(isIn('e', 'abcdefxyz'))
print(isIn('c', 'abcdefxyz'))
print(isIn('g', 'abcdefxyz'))