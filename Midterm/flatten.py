# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 06:58:36 2018

@author: sushy
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
     #the copy of aList which we will return
    flatList = []
    for l in aList:
        if type(l) == list:
            #since it's another list flatten it and then append to our copy
            flatL = flatten(l)
            for el in flatL:
                flatList.append(el)
        else:
            flatList.append(l)
            
    return flatList


test1 = [0, 1, 3, 5, 9, 15, 24, [1, 2, 3, 4, 5, 6, 7]]
test2 = [['hi'], [1, 2, 3, 4, 5], ['hello', 'world'], [0, 2]]
test3 = [['h', ['ello', 'wor'], 'l', ['d']], [0, [1], [2, 3, [4, 5]]], 'lists', ['within', ['lists']]]

#print(flatten(test1)) #this works
#print(flatten(test2))
print(flatten(test3))