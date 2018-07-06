# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 01:26:41 2018

@author: sushy
"""

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(sW, lG):
    '''
    sW - the secret world
    lG - letters guessed by user
    returns true if all the letters guessed are in the secret word and false otherwise
    '''
    
    #first we want to create a list which contians all of the unique letters in secret word
    uniqueLetters = []
    for c in sW:
        if c not in uniqueLetters:
            uniqueLetters.append(c)
            
    
    #then using that list, if any of the letters in letters guessed is in our unique letters list, delete that letter
    for l in lG:
        if l in uniqueLetters:
            uniqueLetters.remove(l)
    
    #if all the letters guessed were in the unique letters list, then it should have length 0. Otherwise the word was not guessed
    if len(uniqueLetters) == 0:
        return True
    else:
        return False


print("The secret word is " + secretWord)
print("Was the word guessed? " + str(isWordGuessed(secretWord, lettersGuessed)))
