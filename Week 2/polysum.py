# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 13:32:04 2018

@author: sushy
"""

import math #importing math library for tan function and pi constant

#polysum function
def polysum(n, s):
    '''
    n: int for number of sides of regular polygon
    s: the length of the sides of regular polygon
    
    returns the sum of perimeter squared and area, rounded to 4 decimal places
    '''
    
    #internal function to calculate area
    def area(n, s):
        '''
        n: same as before, number of sides
        s: the length of the sides
        returns the area of polygon using formula given
        '''
        return (0.25*n*(s**2))/(math.tan((math.pi/n)))
    #internal function to calculate perimeter
    def perim(n, s):
        '''
        n: same as before
        s: same as before
        returns perimeter
        '''
        return n*s
    
    return round((perim(n, s)**2) + area(n, s),4) #square perimeter, add that value to area and then round to 4 decimal places