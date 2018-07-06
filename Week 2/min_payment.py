# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 03:13:36 2018

@author: sushy
"""

            

def findMinPayment(b, r):
    '''
    b - initial balance
    r - annual interest rate
    returns min payment to pay off balance as multiple of 10
    '''
    #helper function for geometric sum
    def geoSum(firstTerm, rate, n):
        if rate > 1:
            return firstTerm* (((rate**n) - 1)/(rate - 1))
        elif rate < 1:
            return firstTerm* ((1 - (rate**n))/(1 - rate))
        else:
            print("Cannot sum")
    
    minPay = 0
    endBalance = 1
    while endBalance > 0:
        minPay+=10
        endBalance = b*((1 + r/12.0)**12) - minPay*(geoSum(1 + r/12.0, 1 + r/12.0, 12))
        
        
        
    
    return minPay

print("Lowest Payment: " + str(findMinPayment(4773, 0.2)))
