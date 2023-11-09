#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:58:54 2023

@author: andrewkwok
"""

from random import randint

class Game:
    name = ""
    price = 0.0
    quantity = 0
    rating = 0.0
    def __init__(self, n, p, q, r):
        self.name = n
        self.price = p
        self.quantity = q
        self.rating = r
    def updatePrice(self, newPrice):
        self.price = newPrice
    def sell(self, price):
        self.quantity -= price
        
    def restock(self, addl_units):
        self.quantity += addl_units
        
    def changeName(self):
        self.name = input("Please enter updated name: ")
        
    def listAttributes(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Rating:", self.rating)
      
def addGame():
    """
    addGame creates a Game object, asking for each attribute one-by-one
    
    Returns
    -------
    Game
        The new game
    """
    name = input("What's the name of the game? ")
    price = float(input("How much does " + name + " cost? "))
    quantity = int(input("How many units of " + name + " are available? "))
    rating = float(input("What is the rating of " + name +  "? "))
    return Game(name, price, quantity, rating)
    
def comparePrice(a, b):
    """
    comparePrice takes two Game objects, gets the price, and compares them

    Returns
    -------
    Game
        The less expensive game
    
    int
        -1 if games are the same price
    """
    if a.price > b.price:
        return b
    elif b.price > a.price:
        return a
    else:
        return -1

def compareRating(a, b):
    """
    compareRating takes two Game objects, gets the rating, and compares them

    Returns
    -------
    Game
        The higher rated game
    int
        -1 if games have the same rating
    """
    if a.rating > b.rating:
        return a
    elif b.rating > a.rating:
        return b
    else:
        return -1

def discount(game):
    """
    discount takes a Game object, asks for a discount rate, then updates price using updatePrice
    """
    discount = float(input("What is the discount percentage? Enter as a percent (0-100): "))
    discount /= 100
    newPrice = (1-discount)*game.price
    game.updatePrice(newPrice)
    print(game.name, "now costs", game.price)

def recommend(a, b):
    """
    recommend takes two Game objects, compares them using comparePrice and compareRating, and prints recommendations based on function calls
    """
    better_rating = compareRating(a, b)
    better_price = comparePrice(a, b)
    if better_rating == -1:
        if better_price != -1:
            print(better_price.name, "is our recommendation.")
        # if both better_rating and better_price return -1, both games have same rating and same price
        else:
            print("Both games are equally good!")
    #called when one game has a better rating than the other
    else:
        #if price is the same
        if better_price == -1:
            print(better_rating.name, "is our recommendation.")
        elif better_price.name == better_rating.name:
            print(better_price.name, "is our recommendation.")
        #if better_price and better_rating are different
        else:
            print(better_price.name, "has a better price, but", better_rating.name, "is better rated.")

def randomGame(inventory):
    """
    randomGame takes the list of games and takes one at random
    
    Returns
    -------
    Game
        The random game picked from inventory
    """
    index = randint(0, len(inventory)-1)
    pick = inventory[index]
    return pick

def main():
    inventory = []
    n_games = int(input("How many games are in the store? "))
    for i in range(n_games):
        inventory.append(addGame())
    if input("Would you like to add a game? ") == "yes":
        inventory.append(addGame())
    if input("Are any games on sale? ") == "yes":
        sale_name = input("Which game is on sale? ")
        for i in inventory:
            if i.name == sale_name:
                discount(i)
                break
    if input("Would you like to compare games? ") == "yes":
        game1 = input("What is the first game? ")
        for i in inventory:
            if i.name == game1:
                game1 = i
                break
        game2 = input("What is the second game? ")
        for i in inventory:
            if i.name == game2:
                game2 = i
                break
        compare = input("Would you like to compare price or rating? ")
        if compare == "price":
            better = comparePrice(game1, game2).name
        elif compare == "rating":
            better = compareRating(game1, game2).name
        print(better, "has the better", compare)
    if input("Would you like to choose a random game? ") == "yes":
        print(randomGame(inventory).name, "is the random game.")
    if input("Would you like a game recommendation? ") == "yes":
        game1 = input("What is the first game? ")
        for i in inventory:
            if i.name == game1:
                game1 = i
                break
        game2 = input("What is the second game? ")
        for i in inventory:
            if i.name == game2:
                game2 = i
                break
        recommend(game1, game2)
    if input("Would you like to list a game's specs? ") == "yes":
        game = input("Which game? ")
        for i in inventory:
            if i.name == game:
                i.listAttributes()
    if input("Have any games been sold? ") == "yes":
        name = input("Which game? ")
        sold = int(input("How many units have been sold? "))
        price = 0
        for i in inventory:
            if i.name == name:
                i.sell(sold)
                price = i.price
                break
        print("You made", price*sold, "dollars.")
    if input("Have you restocked any games? ") == "yes":
        name = input("Which game? ")
        addl_units = int(input("How many units have been added? "))
        for i in inventory:
            if i.name == name:
                i.restock(addl_units)
                break
main()
    
    