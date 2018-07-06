# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:22:56 2018

@author: sushy
"""

s = 'azcbobobegghakl'
numBob = 0

for i in range(len(s)):
    if s[i: i+3] == 'bob':
        numBob +=1

print("Number of times bob occurs is: ", numBob)