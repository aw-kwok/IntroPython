# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:21:52 2023

@author: PSB
"""
import requests
import csv

# import numpy as np    #This line is for Part 5 (which is optional)
# import pandas as pd   #This line is for Part 5 (which is optional)

def getOscarData(url):
    ratingsList = [] 
    titlesList = []
    votesList = []
       
    """
        Part 1: Add lines here to be able to get the source code from
                the desired url and then split that string into a list
                of lines (replacing the assignment below so that lineList
                is a list that holds all the lines in the source code)
    """
    response = requests.get(url)
    source_code = response.text.split("\n")
    
    lineList = []
    
    for line in source_code:
        lineList.append(line)
    
    numLines = len(lineList)
    

    for i in range(numLines):
        if "ratings-imdb-rating" in lineList[i]:
            strippedLineForRating = lineList[i].strip()
            startIndex = strippedLineForRating.index("=",strippedLineForRating.index("data-value"))+2
            endIndex = strippedLineForRating.index(">")
            num = strippedLineForRating[startIndex:endIndex]
            floatNum = float(num.strip("\""))
            ratingsList.append(floatNum)
        
        
        """
            Part 2: Add lines here to extract the titles of each Oscar film
                    and then append each one to the titlesList
                    HINT: each title appears on a line that contains "img alt"
                    HINT: to get the startIndex, you could find the index of
                            a quotation mark (lineList[i].index('\"') and add 1)
        """
        if "img alt" in lineList[i]:
            startIndex = lineList[i].index("=") + 2
            endIndex = lineList[i].rfind('"')
            title = lineList[i][startIndex:endIndex]
            titlesList.append(title)


        """
            Part 4: Add lines here to extract the number of IMDB votes for each 
                    Oscar film and then append each one to the votesList
                    HINT: each vote total appears on *the line after* 
                                            a line that contains "Votes:</span>"
                    HINT: if you strip the appropriate line of white space characters
                                            the startIndex will be 27
                    HINT: if you strip the appropriate line of white space characters
                                            you could find the endIndex by finding the 
                                            index of ">" and then subtracting 1
                                
        """            
            

            
    return ratingsList, titlesList
        
def main():
    webpage = "https://www.imdb.com/search/title/?count=100&groups=oscar_best_picture_winners&sort=year,desc"
    ratingsData, titlesData = getOscarData(webpage)
    
    """
        Part 3: Add lines here to create (i.e., write) a new csv file named
                "imdbDataOutput.csv" in which the first column contains the 
                film titles and the second column contains their ratings.
                
                Part 4 calls for some additional work here.
    """
    
    with open("imdbDataOutput.csv", "w") as f:
        fieldnames = ["Title", "Rating"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        
        writer.writeheader()
        for i in range(len(ratingsData)):
            writer.writerow({"Title": titlesData[i], "Rating": ratingsData[i]})
        
    
    """
        Part 5: Add lines here to use numpy and/or pandas to perform some
                analysis on the data (e.g., correlation between ratings and votes)
    """
    
    
    
    
    
main()






