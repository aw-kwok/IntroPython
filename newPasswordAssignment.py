# -*- coding: utf-8 -*-
"""
Name
Group members (first names):
COSC-010
New Password Lab
"""
import requests
import random


def main():
    #This first line generates a list of user information
    userInfo = [getUserID(), 
                getDateOfBirth(),
                getPassword()]
    #
    #Part 1: In a single line, initialize three variables from
    #           from UserInfo: usr, dob, pswd
    #               - Hint: use indexing
    usr = userInfo[0]
    dob = userInfo[1]
    pswd = userInfo[2]

    #           Print each of the values out. The DOB should be
    #           in a nice format (e.g., February 29, 1989)
    #               -Hint: again, use indexing here
    #
    print("User ID:", usr)
    print("Date of Birth:", dob[0], dob[1] + ",", dob[2])
    print("Current Password:", pswd)
    
    pswd = changePassword()
    print("New Password: ", pswd)
    
    wordFun()
    

def getUserID():
    """
    This function collects the userID from the
    user and returns it.
    
    Returns
    -------
    userID : TYPE str
    """
    userID = input("Enter your user ID: ")
    return userID

def getPassword():
    """
    This function collects the current password from
    the user and returns it. 
    
    Returns
    -------
    password : TYPE str
    """
    password = input("Enter your current password: ")
    return password

def getDateOfBirth():
    """
    This function collects three pieces of info from the
    user regarding their date of birth: Month, Day, Year.
    It then puts these individual items together in the 
    form of a tuple and returns that tuple.    
    
    Returns
    -------
    dateOfBirth : TYPE tuple
    """

    print("Enter your date of birth as follows:")
    month = input("Enter the month: ")
    day = input("Enter the day: ")
    year = input("Enter the year: ")
    
    dateOfBirth = (month, day, year)    

    return dateOfBirth

def changePassword():
    """
    This function refers to a dictionary on the web
    to get a list of words with which it will generate
    a random password. It then gets 3 random words. 
    Then it asks the user whether the words should be 
    capitalized. Then it asks the user what kind of 
    punctuation should be used to separate the words:
    Period (.), Dash (-), Underscore (_) or None. Then
    it concatenates it all together into one string and
    returns that string as the new password.

    Returns
    -------
    newPassword : TYPE str
    """
    newPassword = ""
    response=requests.get("http://www.mit.edu/~ecprice/wordlist.10000")
    txt = response.text #This will be a string containing all the words
    #
    # Part 2a: Generate a list of words and then use random.choice() to 
    #           initialize 3 random words.
    #
    txt = txt.split()
    word1 = random.choice(txt)
    word2 = random.choice(txt)
    word3 = random.choice(txt)
    print("Time for a new password!")
    print("Your new password will be a sequence of random words")
    #
    # Part 2b: Now provide the user the option to capitalize each of the 
    #           3 random words, as well as four options for separating the
    #           words: Period (.), Dash (-), Underscore (_) or None. 
    #           Finally, concatenate it all together to create newPassword
    #           
    #
    caps = input("Would you like to capitalize the first letter of each random word? ")
    
    if caps == "Yes":
        word1 = word1.capitalize()
        word2 = word2.capitalize()
        word3 = word3.capitalize()
    
    delimiter = input("Choose delimiter: Period, Dash, Underscore, or None: ")
    if delimiter == "Period":
        delimiter = "."
    elif delimiter == "Dash":
        delimiter = "-"
    elif delimiter == "Underscore":
        delimiter = "_"
    elif delimiter == "None":
        delimiter = ""
    
    newPassword = word1 + delimiter + word2 + delimiter + word3
        
    return newPassword

def wordFun():
    """
    This function will use the same dictionary as in the changePassword
    function. It will first print out every word in the dictionary that
    begins and ends with the same letter. It will then print out every
    palindrome in the dictionary.

    Returns
    -------
    newPassword : TYPE str
    """
    newPassword = ""
    response=requests.get("http://www.mit.edu/~ecprice/wordlist.10000")
    txt = response.text #This will be a string containing all the words
    txt = txt.split()
    
    #
    # Part 3a: The txt variable (assigned above) contains all the words
    #           in the dictionary. Loop through the words and print out
    #           only the words that begin and end with the same letter
    #
    #           -First uncomment the following three lines
    print()     
    print()   
    print("First we'll print out a lot of words:")
    short_txt = []
    for i in txt:
        if i[0] == i[len(i)-1]:
            short_txt.append(i)
            print(i)
            
    #
    # Part 3b: Now print out only the palindromes in the dictionary 
    #
    #           -First uncomment the following 3 lines       
    print()     
    print()     
    print("Now we'll print out only the words that are palindromes:")
    for i in short_txt:
        palindrome = True
        j = 0
        while(j <= len(i) // 2):
            if i[j] != i[len(i)-j-1]:
                palindrome = False
                break
            j += 1
        if palindrome == True:
            print(i)
                
main() #Remember: Don't accidentlally delete this line!