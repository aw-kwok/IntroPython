#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 20:49:52 2023

@author: andrewkwok
"""

import csv
from datetime import date

today = date.today()

def main():
    dataHistory = "P5_KwokAndrew.csv"
    with open(dataHistory, "r") as filehandle:
        dataFrame = csv.DictReader(filehandle)
        print(dataFrame.fieldnames[4])
        finalscores = []
        for i in dataFrame:
            finalscores.append(float(i["final score"]))
        old_average = sum(finalscores)/len(finalscores)
        old_max = max(finalscores)
        print("The average final score is:", old_average)
        print("The maximum final score is:", old_max)
    
    # ask user to keep adding flavors until answer is no
    add = True
    user_add = input("Would you like to add an entry? ")
    if user_add == "no":
        add = False
    newflavors = []
    while add == True:
        flavor = addFlavor()
        #compare flavor final score to average of old scores
        if flavor["final score"] < old_average:
            print(flavor["flavor"] + " is worse than the old average (" + str(old_average) + "), with a score of " + str(flavor["final score"]))
        elif flavor["final score"] > old_average:
            print(flavor["flavor"] + " is better than the old average (" + str(old_average) + "), with a score of " + str(flavor["final score"]))
        else:
            print(flavor["flavor"] + " is perfectly average, with a score of " + str(flavor["final score"]))
        newflavors.append(flavor)
        print()
        user_add = input("Would you like to add another entry? ")
        if user_add == "no":
            add = False
            
    createUpdatedDataHistory(dataHistory, newflavors)
    
    compare = input("Would you like to compare flavors? ")
    if compare == "yes":
        flavor1 = input("Input flavor 1: ")
        flavor2 = input("Input flavor 2: ")
        compareFlavors("P5_outputfile.csv", flavor1, flavor2)
    
def createUpdatedDataHistory(filename, newData):
    """
    createUpdatedDataHistory takes str filename and list newData and iterates over each dict in newData,
    then appends each dict to the csv under filename
    
    Returns
    ------
    
    """
    with open(filename, "r") as filehandle:
        reader = csv.DictReader(filehandle)
        fieldnames = reader.fieldnames
        with open("P5_outputfile.csv", "w") as fnew:
            writer = csv.DictWriter(fnew, fieldnames=fieldnames)
            writer.writeheader()
            #take old data and write to new file
            for i in reader:
                writer.writerow(i)
            #add new data after original data
            for entry in newData:
                writer.writerow(entry)

def addFlavor():
    """
    addFlavor takes user inputs and creates a dict
    
    Returns
    ------
    dict
        Python dict with keys corresponding to csv headings, values filled by user inputs
    """
    date = today.strftime("%m/%d/%Y")
    name = input("What is the name of the flavor? ")
    sarah = float(input("Sarah, input your score: "))
    andrew = float(input("Andrew, input your score: "))
    final = (sarah + andrew)/2
    return {"date": date, "flavor": name, "sarah's score": sarah, "andrew's score": andrew, "final score": final}
    

def compareFlavors(filename, flavor1, flavor2):
    """
    compareFlavors takes str filename, str flavor1, and str flavor2 to compare final scores of the flavors in the file provided
    
    Returns
    ------

    """
    with open(filename, "r") as filehandle:
        reader = csv.DictReader(filehandle)
        for i in reader:
            if flavor1 == i["flavor"]:
                score1 = i["final score"]
            if flavor2 == i["flavor"]:
                score2 = i["final score"]
        #try/except to account for flavors not in dataset
        try:
            if score1 > score2:
                print(flavor1, "is better than", flavor2, "with a score of", score1)
            elif score2 > score1:
                print(flavor2, "is better than", flavor1, "with a score of", score2)
            else:
                print(flavor1, "and", flavor2, "are scored equally, with a score of", score1)
        except:
            print("A flavor you entered is not in the dataset!")
                
main()