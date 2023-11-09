"""
    Name: Andrew Kwok
    Collaborators: 
    COSC-010
    Cuthbert Assignment

    Code adapted from an original program created by Alphie
    In this program, Cuthbert - a "baker bot" - has 
    a conversation with the user. Cuthbert asks the user for 
    information and then does some impressive calculations.

"""

# By importing time library, the program can have pauses (in this case, to simulate "thinking")
# We can also set a float variable, delay, to set how long each pause will be
#     - Set delay to 0.0 for testing or speed runs
#     - Set delay to larger numbers for dramatic effect. (2.0 = 2 seconds)
import time	
delay = 2.0
foodList = ["muffin", "cookie", "scone", "cake"]
priceList = [2.5, 2.0, 3.0, 25.0]
calorieList = [510, 390, 460, 6500]

print("Hi, I'm Cuthbert the Baker Bot!")

# Each time we want a pause, the program can use the time.sleep() method
time.sleep(delay)		
userName = input("What's your name? ")

time.sleep(delay)
eatOrNot = input("Hi, " + userName + "! Would you like to eat something? ")

"""
    For Part 1...
"""

time.sleep(delay)

#check to see if user wants to eat	
if eatOrNot == "yes":
    foodChoice = input("Okay, what would you like to eat? ")

    time.sleep(delay)
    #check for food availability		
    if foodChoice in foodList:
        print("Great news, " + userName + "! We have a " + foodChoice + " for you!")
        print("The", foodChoice, "has", calorieList[foodList.index(foodChoice)], "calories and costs $ ", priceList[foodList.index(foodChoice)])
    else:
        print("Sorry, " + userName + " - we do not have any " + foodChoice + " for you today.")

"""
    For Part 2...
"""
time.sleep(delay)
inflatedPrices = priceList
print("Bad news. While we've been talking, inflation has made all the prices higher.")
inflationRate = float(input("What is the inflation percentage? "))/100
inflatedPrices = [i*(1+inflationRate) for i in inflatedPrices]

inflatedPricesTotal = sum(inflatedPrices)
originalPricesTotal = sum(priceList)
print("If you ate one of each item, your total would now be", inflatedPricesTotal, "dollars.")
print("In the past, your total would have been", originalPricesTotal )


"""
    For Part 3...
"""
time.sleep(delay)
numItems = len(foodList)
print("We currently have", numItems, "items in our menu.")
time.sleep(delay)
newFoodOrNot = input("Would you like to add anything to the menu? ")

#check if user would like to add new food
if newFoodOrNot == "yes":
    newFood = input("What would you like to add? ")
    foodList.append(newFood)
    priceList.append(float(input("What is the price of this item? ")))
    calorieList.append(float(input("How many calories does this item have? ")))
    numItems += 1
    
removeOrNot = input("Would you like to remove an item? ")
#check to see if user would like to remove item
if removeOrNot == "yes":
    removeFood = input("What is the name of the food you would like to be removed? ")
    #try/except to account for food not found
    try:
        removeFoodIndex = foodList.index(removeFood)
        foodList.remove(removeFood)
        priceList.remove(priceList[removeFoodIndex])
        calorieList.remove(calorieList[removeFoodIndex])
        numItems -= 1
    except:
        print(removeFood, "not found.")

print("We currently have", numItems, "items in our menu.")
totalPrices = sum(priceList)
totalCalories = sum(calorieList)
time.sleep(delay)
print("If you ate one of each item, it would cost", totalPrices, "dollars and be", totalCalories, "calories.")
time.sleep(delay)
print("Bon appetit!")


