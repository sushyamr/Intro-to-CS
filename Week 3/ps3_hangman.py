# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(sW, lG):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
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



def getGuessedWord(sW, lG):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
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
    
    
    #then want to delete letters from alpha that have been guessed already
    for c in lG:
        alpha.remove(c)
    
    
    #return the modified list of letters as a string
    return ''.join(alpha)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses  = 8 #number of mistakes player has left
    lettersGuessed = [] #list for guessed letters
    guessed = False #whether the word has been guessed or not
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    print("-----------")
    
    #want to use a while loop to count down the number of turns
    
    while guesses > 0 and guessed == False:
        print("You have " + str(guesses) + " guesses left")
        letters = getAvailableLetters(lettersGuessed)
        print("Available Letters: " + letters)
        guess = input("Please guess a letter : ")
        
        #wrong guess
        if guess not in secretWord:
            #if it is not guessed already print out that it is a wrong guess, add to letters guessed, print out the word and 
            #subtract one turn from guesses
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                guesses -= 1
            else: #you've already guessed that letter. still print out word but don't add to letters guessed again and don't subtract one turn
                print("Oops! You've already guessed thaet letter: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord: #so a correct guess. once again check if it has already been guessed. if not add to letters guessed
            #then print out information and finally subtract one from turns
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                
            else: #already guessed that letter. so tell player that and don't take away a turn
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        
        print("-----------")
        
        #then check if the word was guessed
        guessed = isWordGuessed(secretWord, lettersGuessed)
        #if guessed is still false, the loop continues, if it's true we break
    
    #display the right message
    if guessed == True:
        print("Congratulations, you won!")
    elif guesses == 0:
        print("Sorry you ran out of guesses. The word was " + secretWord)

        
        
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
