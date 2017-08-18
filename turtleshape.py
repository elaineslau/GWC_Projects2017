from turtle import *
import math

billy = Turtle()

setup(500,300)
x_pos = -250
y_pos = -150

billy.penup()
billy.setposition(x_pos, y_pos)

### Write your code below:
def draw_shape(sides, length):
    exterior_angle = 180-((180*(sides-2)/sides))
    billy.pendown()
    billy.speed(10)

def more (sides, length, x, y):

    xloc = x
    yloc = y

# Close window on click.
exitonclick()
