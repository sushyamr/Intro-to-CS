# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 04:38:14 2018

@author: sushy
"""

guess = 50
high = 100
low = 0
step = guess//2
guessed = False

print("Please think of a number between 0 and 100!")

while guessed == False:
    print("Is your secret number " + str(guess) + "?")
    choice = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if choice != 'h' and choice!='l' and choice!='c':
        print("Please enter your choice properly.")
    elif choice == 'l':
        low = guess
        step = (high - low)/2
        guess = int(guess + step)
    elif choice == 'h':
        high = guess
        step = (high - low)/2
        guess = int(guess - step)
    elif choice == 'c':
        guessed = True

print("Game over. Your secret number was: " + str(guess))
        