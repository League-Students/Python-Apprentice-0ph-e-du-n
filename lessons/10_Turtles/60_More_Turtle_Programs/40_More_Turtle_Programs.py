"""
Copy the code from the previous lesson, 10_More_Turtle_Programs.ipynb,
from the section "Clicking the Turtle Directly"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location

    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
"""

import turtle                               # Import the turtle module

screen = turtle.Screen()                # Set up the screen
screen.setup(width=600, height=600)     # Set the size of the window
screen.bgcolor('white')                 # Set the background color

t1 = turtle.Turtle()                    # Create the first turtle
t1.penup()                              # Lift the pen to move without drawing
t1.shape("turtle")                      # Set the shape of the turtle

t2 = turtle.Turtle()                    # Create the second turtle
t2.penup()                              # Lift the pen to move without drawing
t2.shape("arrow")                       # Set the shape of the turtle

# Move both turtles in a loop
for i in range(-200, 200):
    t1.goto(i, i)
    t2.goto(i, -i)