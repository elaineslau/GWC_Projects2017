from turtle import *
import math

billy = Turtle()

setup(300,300)
x_pos = 0
y_pos = 0

penup()
setposition(x_pos, y_pos)

### Write your code below:
def draw_shape():
    pendown()
    pencolor("blue")
    for counter in range (sides):
        forward(50)
        right(360/sides)
        speed (10)

input_text = input ("How many sides would you like?")
sides = int (input_text)
draw_shape()
# Close window on click.
exitonclick()
