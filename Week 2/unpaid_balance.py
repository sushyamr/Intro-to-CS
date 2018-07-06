# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 01:26:46 2018

@author: sushy
"""

month = 0

def unpBalance(m, b, rInt, rPay):
    '''
    m - month
    b - outstanding balance
    rInt - annual interest
    rPay - min monthly payment rate
    returns unpayed balance after m months
    '''
    
    #helper function to calculate monthly balance
    def calBalance(m, b, rInt, rPay):
        monBalance = b*((1 + (rInt/12.0))*(1 - rPay))**(m+1)
        #print("The blance for month" + str(m) + " is " + str(monBalance))
        return round(monBalance,2)
    
    #helper functio nto calculate min monthly payment
    def minPayment(m, b, rInt, rPay):
        minPayment = b*(((1 + (rInt/12.0))*(1 - rPay))**m)*(rPay)
        print("The minimum monthly payment for month " + str(m) + " is " + str(minPayment))
        return minPayment

    
    return calBalance(m-1, b, rInt, rPay)



print("Remaining balance is: " + str(unpBalance(12, 42, 0.2, 0.04)))