"""
# 30_Turtle_Tricks.py

In this assignment, you will use Tina the Turtle to draw multiple shapes on the screen.

- Draw two circles, each filled with a different color.
- Position the circles in different locations on the screen (they should not overlap).
- Use the turtle commands: begin_fill(), end_fill(), fillcolor(), circle(), and goto() to complete the task.
- Try different colors and positions.

Refer to the previous program, Meet_Tina.py for examples of how to use these turtle commands.
"""

# These lines are needed in most turtle programs
import turtle            # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

tina.goto(50,50)
tina.begin_fill()
tina.circle(25)
tina.fillcolor('blue')
tina.end_fill()

tina.goto(-100,20)
tina.circle(25)
tina.begin_fill()
tina.fillcolor('royal blue')
tina.end_fill()


# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes

... # Your code here

turtle.exitonclick()                    # Close the window when we click on it

# Save your progress by checking in your code.