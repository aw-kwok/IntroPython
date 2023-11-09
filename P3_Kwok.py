#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 23:17:33 2023

@author: andrewkwok
"""

import time
import random

WAIT_TIME = 0.1
APPLE_HP = 20

#initialize variables
inventory = []
hp = 100
gameover = False
monster_1_hp = 50
monster_2_hp = 60
monster_2_inventory = []

#set up story
print("**You wake up in a dark forest. There's nothing in sight, except for a dim orange light in the distance.**")
time.sleep(WAIT_TIME)
print("**You start to walk toward the faint glow. As you get closer, you start to see the silhouette of a small hut. It's starting to get warmer.**")
time.sleep(WAIT_TIME)
print("**You see the shadow of a figure inside.**")

knock = input("**Knock? [yes/no] ").lower() # check lowercase response to remove case sensitivity
if knock == "yes":
    print("**You knock gently on the door.**")
    time.sleep(WAIT_TIME)
    print("**The door opens slowly, and you're greeted by... something. You come to the conclusion that it's a gnome.**")
    time.sleep(WAIT_TIME)
    print("Greetings, traveler! Wow, I haven't seen a newcomer in years!")
    time.sleep(WAIT_TIME)
    name = input("What's your name? \n")
    print("Nice to meet you " + name + "!")
    time.sleep(WAIT_TIME)
    print("This forest is filled with scary creatures!")
    time.sleep(WAIT_TIME)
    print("It's dangerous to go alone!", end = " ")
    time.sleep(WAIT_TIME)

    stick = input("Would you like to take this stick? [yes/no] ").lower() # check lowercase response to remove case sensitivity
    if stick == "yes":
        inventory.append("stick")
        print("Very well, here you go!")
        time.sleep(WAIT_TIME)
        print("**You put the stick in your inventory**")
    else:
        print("Are you sure? It's dangerous to go alone!")
        time.sleep(WAIT_TIME)
        stick = input("**Do you take the stick?** [yes/no] ").lower()
        if stick == "yes":
            inventory.append("stick")
            print("You've made a wise decision!")
            print("**You put the stick in your inventory**")
        else:
            print("Okay, I'll keep the stick.")
    time.sleep(WAIT_TIME)
    print("It was nice to meet you, good luck on your adventure!")
    
print("**You walk out of the house.**")
time.sleep(WAIT_TIME)
apple = input("**You see an apple on the ground. Pick it up? [yes/no] ").lower()
if apple == "yes":
    inventory.append("apple")
    print("**You pick up the apple**")
else:
    print("**Okay, you pass up the apple.**")
    

#monster_1 fight sequence    
time.sleep(WAIT_TIME)
print("**A monster jumps you!**")
time.sleep(WAIT_TIME)
while monster_1_hp > 0: #check to see if monster is alive
    battle = input("**What do you do?** [attack/run] ").lower() #change to lower to remove case sensitivity
    if battle == "attack":
        if len(inventory) != 0:
            print("**Your inventory contains:**")
            for i in inventory:
                print(i)
                time.sleep(WAIT_TIME)
            attack = input("**What do you want to attack with?** ").lower()
            if attack == "stick" and "stick" in inventory:
                print("**You wack the monster with the stick!**")
                time.sleep(WAIT_TIME)
                monster_1_hp -= 50
                print("**The monster keels over and dies.**")
                time.sleep(WAIT_TIME)
                print("**The stick broke!**")
                inventory.remove("stick")
                time.sleep(WAIT_TIME)
                print("**You have a cut down your arm. -20 HP.**")
                hp -= 20
                break
            elif attack == "apple" and "apple" in inventory:
                print("**You throw the apple at the creature from a distance. The monster takes 20hp of damage.**")
                monster_1_hp -= 20
                inventory.remove("apple")
                print("**The monster now has " + str(monster_1_hp) + "hp.**")
            else:
                print("**Attack not valid, try again!**")
        else:
            print("**You have no attack options! The monster gets to you!**")
            print("GAME OVER")
            gameover = True
            break
    else:
        print("**You attempt to run. You get away, but the monster hit you with a stray rock. -10HP. **")
        hp -= 10
        break



#only continue if not gameover
if gameover == False:
    #check to see whether or not the player killed the monster
    time.sleep(WAIT_TIME)
    if monster_1_hp <= 0:
        print("**The creature dropped a bag of loot!**")
        time.sleep(WAIT_TIME)
        print("**The bag contains 3 gold coins, a flashlight, and a box of matches. You add these to your inventory.**")
        inventory.extend(["gold coin", "gold coin", "gold coin", "flashlight", "matches"])
    time.sleep(WAIT_TIME)
    #ask to heal
    if hp < 100 and ("apple" in inventory):
        heal = input("**You are wounded. Would you like to heal?** [yes/no] ").lower()
        if heal == "yes":
            print("**You eat the apple. +" + str(APPLE_HP) + "HP.**")
            inventory.remove("apple")
            hp += APPLE_HP
            #if we increased the hp that eating the apple heals (APPLE_HP) make sure hp is not over 100
            if hp > 100:
                hp = 100
    time.sleep(WAIT_TIME)
    print("**Your hp is "+ str(hp) + ".**")
    time.sleep(WAIT_TIME)
    print("**Your inventory is:")
    for i in inventory:
        print(i)
    time.sleep(WAIT_TIME)
    print("**Another monster appears! It copies your inventory!")
    monster_2_inventory = [i for i in inventory] # use list comprehension so that monster_2_inventory doesn't point to inventory
    time.sleep(WAIT_TIME)
    #monster 2 attack sequence
    while monster_2_hp > 0:
        if hp == 0:
            print("**Your HP has depleted to 0. Game over!**")
            gameover = True
            break
        if "gold coin" in monster_2_inventory:
            print("**The monster throws a gold coin at you! -40HP.")
            monster_2_inventory.remove("gold coin")
            hp -= 40
        if len(inventory) != 0:
            print("**The monster steals a random item from your inventory!**")
            steal = random.randint(0, len(inventory) - 1)
            time.sleep(WAIT_TIME)
            print("**The monster stole " + inventory[steal] + " from you!**")
            monster_2_inventory.append(inventory[steal])
            inventory.remove(inventory[steal])
            time.sleep(WAIT_TIME)
            print("**Your inventory now contains:")
            for i in inventory:
                print(i)
        time.sleep(WAIT_TIME)
        battle = input("**What do you do?** [attack/run] ").lower() #change to lower to remove case sensitivity
        if battle == "attack":
            if len(inventory) != 0:
                print("**Your inventory contains:")
                for i in inventory:
                    print(i)
                time.sleep(WAIT_TIME)
                attack = input("**What do you want to attack with?** ").lower()
                if attack == "gold coin" and "gold coin" in inventory:
                    print("**You throw a gold coin at the monster!**")
                    time.sleep(WAIT_TIME)
                    monster_2_hp -= 40
                    print("**The monster loses 40HP!**")
                    time.sleep(WAIT_TIME)
                    print("**The monster now has " + str(monster_2_hp) + "hp.**")
                    inventory.remove("gold coin")
                    time.sleep(WAIT_TIME)
                elif attack == "apple" and "apple" in inventory:
                    print("**You throw the apple at the creature from a distance. The monster takes 20hp of damage.**")
                    monster_2_hp -= 20
                    inventory.remove("apple")
                    time.sleep(WAIT_TIME)
                    print("**The monster now has " + str(monster_2_hp) + "hp.**")
                else:
                    print("**Invalid option, try again!**")
                    time.sleep(WAIT_TIME)
            else:
                print("You have no items left in your inventory! The monster gets to you! Game over!")
                gameover = True
                break
        else:
            print("**You attempt to run. The monster gets to you. Game over!**")
            gameover = True
            break

time.sleep(WAIT_TIME)
if gameover == False:
    print("**You made it!**")
    print("Thanks for playing!")
else:
    print("Unfortunately you lost, but thanks for playing!")