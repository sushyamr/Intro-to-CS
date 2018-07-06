# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:19:00 2018

@author: sushy
"""

s = 'azcbobobegghakl'
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
        or char == 'o' or char == 'u' :
            numVowels+=1

print("Number of vowels: ", numVowels)