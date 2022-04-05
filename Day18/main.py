import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
# timmy.shape("")
# timmy.color("red")


## To create a dashed line

# for _ in range(11):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

## To draw triangle, square, pentagon, hexagon, octagon ....
# colors = ["red", "blue", "black", "orange", "green", "pink"]
#
# def draw_shape(side):
#     Angle = 360
#     for _ in range(side):
#         timmy.forward(100)
#         timmy.right(Angle / side)
#     side += 1
#
# for sides in range(3, 11):
#     timmy.color(choice(colors))
#     draw_shape(sides)

## Draw a random walk
# colors = ["crimson", "indigo", "darkblue", "orange", "green", "pink", "grey", "fuchsia", "aqua", "coral", "magenta"]
# angles = [90, 180, 270, 360]
# timmy.width(8)
# timmy.speed(speed=10)
#
# for _ in range(150):
#     timmy.color(random.choice(colors))
#     timmy.forward(20)
#     # timmy.right(random.choice(angles))
#     timmy.setheading(random.choice(angles))

## Draw a circle like Spirograph

colors = ["crimson", "indigo", "darkblue", "orange", "green", "pink", "grey", "fuchsia", "aqua", "coral", "magenta"]

Angle = 360
timmy.speed(speed="fastest")
head = timmy.heading()

for _ in range(100):
    timmy.color(random.choice(colors))
    timmy.circle(100)
    timmy.setheading(head)
    head += 4

screen = Screen()
screen.exitonclick()
