#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:48:13 2023

@author: andrewkwok
"""
from party import PartyAnimal

class Bulldog(PartyAnimal):
    what = 1789
    def rocks(self):
        self.what *= 2
        self.x += self.what
        print("What counter:", self.what)

def main():
    s = Bulldog()
    j = Bulldog()
    
    count = 0
    for i in range(10):
        count += 1
        person = input("Choose Sally or Jim: ")
        if person == "Sally":
            person = s
        else:
            person = j
        choice = input("Choose party or sleep: ")
        if choice == "party":
            if count % 2 == 0:
                person.party()
            else:
                person.rocks()
        else:
            person.sleep()

    if s.getDifference() > j.getDifference():
        print("Sally is a bigger party animal than Jim.")
    elif j.getDifference() > s.getDifference():
        print("Jim is a bigger party animal than Sally.")
    else:
        print("Sally and Jim are equal party animals.")

main()