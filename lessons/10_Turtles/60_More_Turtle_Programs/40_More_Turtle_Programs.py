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

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path                        # Import Path from pathlib module
    image_dir = Path(__file__).parent.parent / "images"    # Define the directory containing images
    image_path = str(image_dir / image_name)        # Create the full path to the image file

    screen = turtle.getscreen()                     # Get the turtle's screen
    screen.addshape(image_path)                     # Register the image as a shape
    turtle.shape(image_path)                        # Set the turtle's shape to the image

t1 = turtle.Turtle()                    # Create the first turtle
t1.penup()                              # Lift the pen to move without drawing
t1.shape("turtle")                      # Set the shape of the turtle

t2 = turtle.Turtle()                    # Create the second turtle
t2.penup()                              # Lift the pen to move without drawing
set_turtle_image(t, "leaguebot_bolt.gif")                       # Set the shape of the turtle

# Move both turtles in a loop
for i in range(-200, 200):
    t1.goto(i, i)
    t2.goto(i, -i)