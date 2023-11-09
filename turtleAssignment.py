"""
Name: Andrew Kwok
Group members (first names):
COSC-010
Turtle Assignment
"""
from turtle import *  # Necessary here at the beginning in order to use Turtle

clear()
print("Part 0")
#
# Part 0: Add lines here
#
penup()
goto(-200, 200)
write("Andrew")
goto(0, 0)


# Now onto the rest of the program...
print("Part 1")
    
# The following four lines assign values to our VARIABLES
xStart = -30        # the x-coordinate of square's starting location
yStart = 50         # the y-coordinate of square's starting location
sideLength = 75     # the length of each side of the square
color = "gray"      # the color for the square 

fillcolor(color)   # Tell Turtle what color to make the square

#
# PART 1: Add lines here
#

goto(xStart,yStart)
pendown()
begin_fill()
goto(xStart+sideLength,yStart)
goto(xStart+sideLength,yStart-sideLength)
goto(xStart,yStart-sideLength)
goto(xStart,yStart)
penup()
end_fill()
    


print("Part 2")  
xStart = 100	#Update the x-coordinate for the second square
yStart = -50   	#Update the y-coordinate for the second square
#
# PARTS 2: Add lines here
#
print()

choice = input("Do you want the second square to be a different color? ")

if (choice == "yes"):
    color = "blue"
    
fillcolor(color)
    
goto(xStart,yStart)
pendown()
begin_fill()
goto(xStart+sideLength,yStart)
goto(xStart+sideLength,yStart-sideLength)
goto(xStart,yStart-sideLength)
goto(xStart,yStart)
penup()
end_fill()


print("Part 3")
#
# PARTS 3: ADD LINES HERE
#
print()
color = input("Enter a color: ")
xStart = eval(input("Enter a number between -100 and 100: "))
yStart = eval(input("Enter a number between -100 and 100: "))
sideLength = eval(input("Enter a number between 30 and 100: "))

fillcolor(color)
    
goto(xStart,yStart)
pendown()
begin_fill()
goto(xStart+sideLength,yStart)
goto(xStart+sideLength,yStart-sideLength)
goto(xStart,yStart-sideLength)
goto(xStart,yStart)
penup()
end_fill()

done()  # Necessary here so that the picture stays visible
bye()   # Necessary so that the Turtle window exits without crashing

