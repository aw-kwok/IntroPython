#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 2 14:17:33 2023

Name: Andrew Kwok
Group members (first names):
COSC-010
Choices Assignment

"""

# initialize variables
fullname = ""
space = 0
lastName = ""
year = ""
paint = ""
renovation = ""
risk = "LOW"

# name input and parse last name
fullName = input("Enter your full name: ")
space = fullName.find(" ")
lastName = fullName[space+1:]

# get user input for year, and keep asking until year is type int
while not(isinstance(year, int)):
    try:
        year = int(input("What year was your residence built? "))
    except:
        print("Please enter an integer")
        print()

#risk assessment
if (year < 1978):
    paint = input("Is the pain in your residence chipping, peeling, or in poor condition? ")
    renovation = input("Is there recent, ongoing, or planned renovcation or remodeling? ")
    if paint == "yes" or renovation == "yes":
        risk = "HIGH"
    else:
        risk = "MEDIUM"

print("Risk level for the", lastName.upper(), "household:", risk) 