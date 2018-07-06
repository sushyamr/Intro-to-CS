# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 01:37:09 2018

@author: sushy
"""

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(sW, lG):
    '''
    sW: string, the word the user is guessing
    lG: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #first want to create a list with all the letters in secret word, so we can change certain letters
    letters = []
    for c in sW:
        letters.append(c)
    
    
    #then for each letter that was not in letters guessed change that to an underscore
    for i in range(len(letters)):
        if letters[i] not in lG:
            letters[i] = ' _ '
    
    
    #then we want to return the string version of letters
    
    return ''.join(letters)
    


print(getGuessedWord(secretWord, lettersGuessed))
        