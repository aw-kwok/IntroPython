#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Name: Andrew Kwok
    Date: March 3, 2023
    Course: COSC-010
    Assignment: Project 2
"""
import time

#initialize variables
delay = 0
age = ""
parent = "no"
consent = False
good_words = ["good", "happy", "calm", "satisfied", "glad", "thankful"]
bad_words = ["bad", "anxious", "sad", "depressed", "angry", "down"]
good_count = 0
bad_count = 0

name = input("Hello! What's your name? ")
time.sleep(delay)
print("Nice to meet you " + name + "!")

# check for age
while not(isinstance(age,int)):
    try:
        time.sleep(delay)
        age = int(input("How old are you? "))
        time.sleep(delay)
    
    #check to see if age is non-negative, if so raise exception
        if age < 0:
            raise Exception()
    except:
        print("That's not a real age!")
        age = ""    # set age to str to run the age check test over
    
if age < 18:
    print("We're gonna need some parental permission! Talking to strangers (even chatbots) is dangerous!")
    time.sleep(delay)
    while parent == "no":
        parent = input("Are you the parental guardian of " + name + "? ").lower()
        time.sleep(delay)
    #check for parental consent
        if parent == "yes":
            parental_consent = input("Do you give consent to your child to use chatbot? ")
            time.sleep(delay)
            if parental_consent.lower() == "yes":
                consent = True
                break
            else:
                print("Sorry, you can't use this chatbot!")
                time.sleep(delay)
                consent = False
                break
        else:
            print("Go get a parent!")
            time.sleep(delay)
else:
    user_consent = input("Do you wish to talk to chatbot? ")
    if user_consent.lower() == "yes":    
        consent = True
    
# run if consent is given
if consent == True:
    print("Great! My name is Chatbot, nice to meet you " + name + "!")
    time.sleep(delay)
    sentiment = input("How are you doing today? ")
    time.sleep(delay)
    
    # split user input into a list of words
    sentiment = list(map(str, sentiment.split(" ")))
    
    # convert all entries in sentiment to lowercase to compare with good_words and bad_words
    sentiment_list = []
    for i in sentiment:
        sentiment_list.append(i.lower())
    
    # tally good words and bad words
    for i in sentiment_list:
        if i in good_words:
            good_count += 1
        elif i in bad_words:
            bad_count += 1
    
    # give response based off of good and bad word count
    if good_count < bad_count:
        print("I'm sorry to hear that.")
        time.sleep(delay)
        print("You're strong, I know you'll get through this!")
    elif bad_count < good_count:
        print("That's good! I'm happy to hear that!")
    else:
        print("Yeah, some days are just like that, I understand.")
    time.sleep(delay)
    print("Sorry, I've got to run, it was nice talking to you!")

# if consent not given, end program        
else:
    print("Sorry, you have not given consent to use chatbot.")