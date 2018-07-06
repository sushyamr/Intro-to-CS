# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 05:03:05 2018

@author: sushy
"""

def minPayment(b, r):
    '''
    b - intial balance
    r - annual interest rate
    returns min payment necessary to pay it off
    '''
    
    low = b/12.0
    high = (b*((1 + r)**12))/12.0
    guess = (high - low)/2
    
    
    
    #helper function for geometric sum
    def geoSum(firstTerm, rate, n):
        if rate > 1:
            return firstTerm* (((rate**n) - 1)/(rate - 1))
        elif rate < 1:
            return firstTerm* ((1 - (rate**n))/(1 - rate))
        else:
            print("Cannot sum")
    
    endBalance = 1
    while abs(endBalance) != 0:
        endBalance = b*((1 + r/12.0)**12) - guess*(geoSum(1 + r/12.0, 1 + r/12.0, 12))
        
        if endBalance > 0: #then guess is too small
            low = guess
            step = (high - low)/2
            guess = guess + step
        elif endBalance < 0: #then guess is too big
            high = guess
            step = (high - low)/2
            guess = guess - step
            
    
    return round(guess, 2)


balance = input("Enter an initial balance: ")
rate = input("Enter an annual interest rate (in decimal): ")

print("Lowest payment: " + str(minPayment(float(balance), float(rate))))