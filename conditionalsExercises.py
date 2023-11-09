#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:40:57 2023

@author: andrewkwok
"""

#initialize variables
hours = ""
rate = ""
pay = 0

#throw error and exit if user does not enter numerical values for hours and rate
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    
    #check to see if overtime was worked and calculate overtime pay if necessary
    if hours > 40:
        pay = 40 * rate + (hours-40)*(rate*1.5)
    else:
        pay = hours * rate
    
    print("Pay:" , pay)
    
except:
    print("Numerical values not entered")