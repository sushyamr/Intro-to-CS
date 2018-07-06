# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 07:05:32 2018

@author: sushy
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    values = aDict.values()
    length = 0
    for s in values:
        length += len(s)
    
    
    return length

def biggest(aDict):
    keys = aDict.keys()
    values = aDict.values()
    
    big = 0
    bigKey = ''
    
    for k in keys:
        if len(aDict[k]) >= big:
            big = len(aDict[k])
            bigKey = k
    
    return k

print("Lenght of dict animals is : " + str(how_many(animals)))
print(animals)
i = 0
for l in animals.values():
    print("Value " + str(i) + " : " + str(l))
    print("Length " + str(i) + " : " + str(len(l)))
    i+=1
    

print("Biggest key: " + str(biggest(animals)))