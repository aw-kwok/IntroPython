"""
Name Andrew Kwok
Group members (first names):
COSC-010
Working with Files Assignment 

"""
from statistics import *
import csv

def part1():
    edFile = open("Choose_Maryland___Compare_Counties_-_Education.csv", "r")
    reader = csv.reader(edFile)
    colNames1 = next(reader)
    edRecords = []
    for row in reader:
        try:
            float(row[1])
            edRecords.append(row)
        except:
            pass
    edFile.close()
    highAttain = []
    for i in edRecords:
        highAttain.append(float(i[5]))
#    print(highAttain)
    print("Mean high school attainment:", mean(highAttain))
    print("Median high school attainment:", median(highAttain))
    print("Standard deviation high school attainment:", stdev(highAttain))
    
    houseFile = open("Choose_Maryland___Compare_Counties_-_Quality_Of_Life.csv", "r")
    reader = csv.reader(houseFile)
    colNames2 = next(reader)
    colNames2.remove("County")
    print(colNames2)
    houseRecords = []
    for row in reader:
        try:
            float(row[1])
            houseRecords.append(row)
        except:
            pass
    houseFile.close()
    homePrice = []
    for i in houseRecords:
        homePrice.append(float(i[2]))
    print("Mean home price:", mean(homePrice))
    print("Median home price:", median(homePrice))
    print("Standard deviation home price:", stdev(homePrice))
    highAttain_max = max(highAttain)
    highAttain_min = min(highAttain)
    index = 0
    while index < len(edRecords):
        if highAttain_max == highAttain[index]:
            print("Max:")
            print("Jurisdiction:", edRecords[index][0])
            print("High school attainment:", highAttain_max)
            print("Average sale price:", homePrice[index])
        elif highAttain_min == highAttain[index]:
            print("Min:")
            print("Jurisdiction:", edRecords[index][0])
            print("High school attainment:", highAttain_min)
            print("Average sale price:", homePrice[index])
        index += 1
        
def part2b():
    name = input("Enter the file name: ")
    text = open(name, "r")
    count = 0
    confidence = 0
    for row in text:
        if "X-DSPAM-Confidence: " in row:
            split_index = row.index(":") + 1
            number = float(row[split_index:].strip())
            count += 1
            confidence += number
    print("Average spam confidence:", confidence/count)
    text.close()

def part2a():
    name = input("Enter a file name: ")
    text = open(name, "r")
    for row in text:
        print(row.upper())
    text.close()

def main():
    """
    The main function in this program just calls the other functions. You can
    comment out any of the function calls here if you just want to see how one
    of the functions is running (and don't want to wait for the rest of the 
    functions to do their thing).
    """
    
    part1()	# Leave uncommented if you want to run the part1() function
    part2a()	# Leave uncommented if you want to run the part2a() function 
    part2b()	# Leave uncommented if you want to run the part2b() function 


main() # We need the call to main here, after all functions have been defined
