# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 02:58:27 2018

@author: sushy
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

