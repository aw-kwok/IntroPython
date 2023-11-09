#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:24:18 2023

@author: andrewkwok
"""

from bs4 import BeautifulSoup
import requests

person = input("What is the name of the person that you'd like to look for? ")

total1 = 0
year = 1
while year < 93:
    response=requests.get("https://en.wikipedia.org/wiki/"+str(year)+"th_Academy_Awards")
    txt = response.text

    count = txt.count(person)
    if count > 0:        
        print (person + " appears " + str(count) + " times on the page for the " + str(year) + "th Oscars")
        total1 += count
    year += 1

person2 = input("Input a person you'd like to compare " + person + " with: ")

total2 = 0
year = 1
while year < 93:
    response=requests.get("https://en.wikipedia.org/wiki/"+str(year)+"th_Academy_Awards")
    txt = response.text

    count = txt.count(person2)
    total2 += count
    year += 1

if total1 > total2:
    print(person + " appears more in total across every Academy Awards Wikipedia Page, with " + str(total1) + " appearances compared to " + person2 + "'s " + str(total2))
elif total1 < total2:
    print(person2 + " appears more in total across every Academy Awards Wikipedia Page, with " + str(total2) + " appearances compared to " + person + "'s " + str(total1))
else:
    print("Both", person, "and", person2, "appear an equal amount across every Academy Awards Wikipedia Page, with", str(total1), "appearances")