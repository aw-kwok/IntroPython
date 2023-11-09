"""
    Name: Andrew Kwok
    Collaborators: 
    COSC-010
    Subtraction Game Assignment

    In this game, the user selects an integer between 10 and 30. This
    number represents the starting number of matches. The user and the
    then alternate removing 1 or 2 matches. The object of the game is 
    to avoid removing the last match. The computer will play without
    much strategy, generally just choosing 1 or 2 at random.
"""
import random
import time
delay = 1

print("Welcome to the Subtraction Game!")

repeat = "yes"
user_input = 0
n = 0

while repeat == "yes":
    while n < 10 or n > 30:
        try:
            n = int(input("Enter the starting number of matches (between 10 and 30) "))
        except:
            print("Enter a valid integer (between 10 and 30)")
    remaining = n

    """

    Insert code here to allow user to select before computer each turn


    """
    while remaining > 0:
        while user_input < 1 or user_input > 2:
            try:
                user_input = int(input("Choose to remove one or two matches: "))
                if user_input == 1 or user_input == 2:
                    remaining -= user_input
                else:
                    raise Exception()
            except:
                print("Please enter a valid answer")
                user_input == 0     #reset user_input to reiterate through check, make sure it's an int so conditional can work
                
        if remaining <= 0:
            print("Computer wins")
            break
        
        print("...And of the original", n, "matches, now there are", remaining, "left")
        user_input = 0  # reset user_input so user input loop runs again
    
        time.sleep(delay * 2)
        computerChoice = random.choice([1, 2])
        print("...The computer chooses", computerChoice)

        """

        Insert code here to deal with the result of computer making its choice

        """
        remaining -= computerChoice
        
        if remaining <= 0:
            print("User wins")
            break
        
        print("...And of the original", n, "matches, now there are", remaining, "left")

    repeat = input("Would you like to play another game? ").lower()
    n = 0
        
print("Thank you for playing. Goodbye.")        
        
            
        