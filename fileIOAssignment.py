#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:18:28 2023

@author: andrewkwok
"""
import csv

linecount = 0
col3_val = []
col3_total = 0
col3_count = 0
\=.
myfile = open("Choose_Maryland___Compare_Counties_-_Education.csv", "r")

fileText = myfile.read()
print(fileText)
myfile.close()

myfile = open("Choose_Maryland___Compare_Counties_-_Education.csv", "r")
reader = csv.reader(myfile)

firstline = next(reader)
linecount += 1

for line in reader:
    linecount += 1
    col3_val.append(line[2])
print(linecount)
print(firstline)
print(firstline[2])

for i in col3_val:
    print(i)
    try:
        i = float(i)
        col3_total += i
        col3_count += 1
    except:
        pass
print(col3_total/col3_count)
myfile.close()