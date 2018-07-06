# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:26:56 2018

@author: sushy
"""

s = 'azcbobobegghakl'

substr = ''


tempstr = ''

for prev, curr in zip(' ' + s, s + ' '):
        if curr < prev:
            if len(tempstr) > len(substr):
                substr = tempstr[:]
            tempstr = ''
        tempstr += curr
        


print("Longest substring is: ", substr)