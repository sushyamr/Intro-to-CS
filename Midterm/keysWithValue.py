# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 06:49:14 2018

@author: sushy
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    
    keys = aDict.keys()
    
    targetKeys = []
    
    for k in keys:
        if aDict[k] == target:
            targetKeys.append(k)
        
    #targetKeys.sort()
    copyKeys = targetKeys.copy()
    sizeKeys = len(targetKeys)
    
    for i in range(sizeKeys):
        if i != sizeKeys - 1:
            if copyKeys[i] > copyKeys[i + 1]:
                targetKeys[i + 1] = copyKeys[i]
                targetKeys[i] = copyKeys[i + 1]
    
        
    
    return targetKeys



testDict = {1:2, 2:4, 3:2, 4:2, 5:8, 6:8, 7:0, 8:6, 9:4, 10:2}

print("Keys with value 2 are: ", keysWithValue(testDict, 2))