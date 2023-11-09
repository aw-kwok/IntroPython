"""
Name Andrew Kwok
Group members (first names):
COSC-010
Wordle Assignment

"""
import random

def main():
    someGuess = "" #initialize someGuess
    guessCount = 0
    secretWord = random.choice(getListOfWords("wordleAnswerWords.txt"))
    incorrectLetters = []
    while guessCount  < 6:
        while len(someGuess) != 5:
            someGuess = input("Enter a five-letter word: ").lower()
        
        evaluation = "xxxxx"
        evaluation = guess(someGuess, secretWord)
        print(someGuess)
        print(evaluation)
        
        incorrectLetters = updateIncorrectLetters(someGuess, secretWord, incorrectLetters)
        print("Incorrect letters so far:", incorrectLetters)
        
        if secretWord.upper() == evaluation:
            print("You win!")
            break
        
        guessCount += 1
        someGuess = ""
    if guessCount == 6:
        print("Sorry - you are out of guesses")
        print("The secret word was", secretWord)

def getListOfWords(fileName):
    myfile = open(fileName, "r")
    fileText = myfile.read()
    myfile.close()
    fileLines = fileText.split("\n")
    return fileLines

def guess(attempt, secret):
    outputString = ""
    i = 0
    while i < 5:
        if attempt[i] in secret:
            if attempt[i] == secret[i]:
                outputString = "".join((outputString, attempt[i].upper()))
            else:
                outputString = "".join((outputString, "o"))
        else:
            outputString = "".join((outputString, "X"))
        i += 1
    return outputString

def updateIncorrectLetters(attempt, secret, letters):
    for i in attempt:
        if i not in secret and i not in letters:
            letters.append(i)
    letters.sort()
    return letters
  
main()