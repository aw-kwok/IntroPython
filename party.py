#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:02:12 2023

@author: andrewkwok
"""

class PartyAnimal:
    x = 0
    y = 0

    def __init__(self):
        print('I am constructed')

    def party(self) :
        self.x = self.x + 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed', self.x)

    def sleep(self):
        self.y += 1
        print('So far', self.y)
        
    def getDifference(self):
        return self.x - self.y
    