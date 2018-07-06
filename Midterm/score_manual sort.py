# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 07:13:26 2018

@author: sushy
"""

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    
    #dictionary mapping a to 1, b to 2, c to 3 etc etc
    alphaDict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13,
                 'n' : 14, 'o' : 15, 'p': 16, 'q' : 17, 'r': 18, 's' : 19, 't': 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x': 24, 'y' : 25, 'z' : 26 }
    
    #make the word all lower case
    word = word.lower()
    
    #then get a list of all the letters in word
    letters = []
    for s in word:
        letters.append(s)
    
    #then score based on the position of the letter and what the letter is. store the individual score in a list
    letterScore = []
    
    for i in range(len(letters)):
        letterScore.append(i*alphaDict[letters[i]])
    
    #then sort the list. This will be in descending order so reverse it to find the two highest scores
    #letterScore.sort()
    #letterScore.reverse()
    copy = letterScore.copy()
    
    for j in range(len(copy)):
        if j != len(copy) - 1:
            if copy[j] < copy[j + 1]:
                letterScore[j + 1] = copy[j]
                letterScore[j] = copy[j + 1]
    
    
    #return f applied to the two highest score
    return f(letterScore[0], letterScore[1])


#for testing def sum (a, b)

def sum(a, b):
    return a + b

print(score('adD', sum))