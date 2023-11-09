"""
    Name: Andrew Kwok
    Date: February 9, 2023
    Course: COSC-010
    Assignment: Project 1
"""

from turtle import *  # Necessary here at the beginning in order to use Turtle


#  Your code goes here...

# initialize variables
GTOWN_BLUE = "#041E42"
GTOWN_GRAY = "#63666A"
TURTLE_GREEN = "#9DFF9A"
X_ORIGIN = 0
Y_ORIGIN = 0

triangle_side_length = ""   #initialized to str to make int check work
square_side_length = ""     #initialized to str to make int check work
user_side_length = ""     #initialized to str to make int check work
user_nsides = ""     #initialized to str to make int check work
polygon_exterior_angle = 0
polygon_interior_angle = 0
user_x = ""     #initialized to str to make int check work
user_y = ""     #initialized to str to make int check work

# clear canvas and pick up pen/fill
clear()
penup()
end_fill()
setheading(0)

# write user inputted string at 500,500
goto(100,-100)
pendown()
write(input("Enter a string you would like displayed: "))
penup()

# gather int value for triangle side length, keep trying until non-zero int is entered
while not(isinstance(triangle_side_length, int)):
    try:
        triangle_side_length = int(input("Enter triangle side length: "))
        1/triangle_side_length  # check if int is non-zero
        
        # change negative integers to positive
        if (triangle_side_length < 0):
            triangle_side_length *= -1
            
    except:
        print("That is not a non-zero integer, please enter a non-zero integer.")
        triangle_side_length = ""   # reset triangle side length to str to int check
        
print("Creating triangle...")

# create triangle in Georgetown Blue
fillcolor(GTOWN_BLUE)
goto(X_ORIGIN - triangle_side_length - 15, Y_ORIGIN) # start triangle so that the right edge is 15 left of 0,0
pendown()
begin_fill()
for i in range(3):
    forward(triangle_side_length)
    left(120)
penup()
end_fill()

print("Georgetown Blue Hex Color:", GTOWN_BLUE)

# gather int value for square side length, keep trying until non-zero int is entered
while not(isinstance(square_side_length, int)):
    try:
        square_side_length = int(input("Enter square side length: "))
        1/square_side_length  # check if int is non-zero
        
        # change negative integers to positive
        if (square_side_length < 0):
            square_side_length *= -1
            
    except:
        print("That is not a non-zero integer, please enter a non-zero integer.")
        square_side_length = ""   # reset square side length to str to int check
        
print("Creating square...")

# create square in Georgetown Gray
fillcolor(GTOWN_GRAY)
goto(X_ORIGIN + 15, Y_ORIGIN) # start square such that left edge is 15 right of 0,0
pendown()
begin_fill()
for i in range(4):
    forward(square_side_length)
    left(90)
penup()
end_fill()

print("Georgetown Gray Hex Color:", GTOWN_GRAY)

# gather int value for user side length, keep trying until non-zero int is entered
while not(isinstance(user_side_length, int)):
    try:
        user_side_length = int(input("Enter side length of the regular polygon you would like to make: "))
        1/user_side_length  # check if int is non-zero
        
        # change negative integers to positive
        if (user_side_length < 0):
            user_side_length *= -1
            
    except:
        print("That is not a non-zero integer, please enter a non-zero integer.")
        user_side_length = ""   # reset user side length to str to int check

# gather int value for number of polygon sides, keep trying until non-zero int is entered
while not(isinstance(user_nsides, int)):
    try:
        user_nsides = int(input("Enter number of sides for the polygon (no triangles or squares!): "))
        1/user_nsides  # check if int is non-zero
        
        # change negative integers to positive
        if (user_nsides < 0):
            user_nsides *= -1
        
        # check to see if side length is greater than 3, raise exception if not
        if (user_nsides < 4):
            raise Exception()
            
    except:
        print("That is not a non-zero integer with magnitude greater than 3, please enter a non-zero integer with magnitude greater than 3.")
        user_nsides = ""   # reset nsides to str to int check

# gather int value for x-location of user-created polygon
while not(isinstance(user_x, int)):
    try:
        user_x = int(input("Enter x-location of polygon: "))
            
    except:
        print("That is not an integer, please enter an integer.")
        
# gather int value for y-location of user-created polygon
while not(isinstance(user_y, int)):
    try:
        user_y = int(input("Enter y-location of polygon: "))
            
    except:
        print("That is not an integer, please enter an integer.")

print("Creating " + str(user_nsides) + "-gon")

polygon_exterior_angle = 360/user_nsides    # calculate exterior angle of polygon
polygon_interior_angle = ((user_nsides-2) * 180)/user_nsides    #calculate interior angle of polygon


# create polygon in Turtle Green
fillcolor(TURTLE_GREEN)
# orient polygon upright: even shapes need no correction, rotate odd shapes
if (user_nsides%2 != 0):
    right(90-(polygon_interior_angle/2))
else:
    user_x -= user_side_length/2 # adjust top middle of shape to be user input
goto(user_x, user_y) # start shape at user-inputted space

pendown()
begin_fill()
for i in range(user_nsides):
    forward(user_side_length)
    right(polygon_exterior_angle)
penup()
end_fill()

print("Turtle Green Hex Color:", TURTLE_GREEN)

done()  # Necessary here so that the picture stays visible
bye()   # Necessary so that the Turtle window exits without crashing