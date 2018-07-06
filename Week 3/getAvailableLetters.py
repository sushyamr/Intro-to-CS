# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 01:46:04 2018

@author: sushy
"""
import string

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def getAvailableLetters(lG):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    #want to create a list with all the letters of the alphabet
    alpha = []
    for c in string.ascii_lowercase:
        alpha.append(c)
    
    print(str(alpha)) #testing
    
    #then want to delete letters from alpha that have been guessed already
    for c in lG:
        alpha.remove(c)
    
    
    #return the modified list of letters as a string
    return ''.join(alpha)


print(getAvailableLetters(lettersGuessed))