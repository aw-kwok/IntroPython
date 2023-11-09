#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:49:22 2023

@author: andrewkwok
"""

import random #imports some new functions that do random calculations

computerChoice = random.choice(['rock','paper','scissors'])#Get random

userChoice = input("Ok, rock, paper; scissors: ")   #Get user’s choice
print("You chose", userChoice)                      #Now start to output result of the game
    
if userChoice == computerChoice:
    print("Computer chose", computerChoice, "- You tie!")
else:
    #computer scissors cases
    if computerChoice == 'scissors':
        if userChoice == 'rock':
            print("Computer chose", computerChoice, "- You win!")
        else:
            print("Computer chose", computerChoice, "- You lose!")
    #computer rock cases      
    if computerChoice == 'rock':
        if userChoice == 'paper':
            print("Computer chose", computerChoice, "- You win!")
        else:
            print("Computer chose", computerChoice, "- You lose!")
    #computer paper cases   
    if computerChoice == 'paper':
        if userChoice == 'scissors':
            print("Computer chose", computerChoice, "- You win!")
        else:
            print("Computer chose", computerChoice, "- You lose!")
        