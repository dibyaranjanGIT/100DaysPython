# import colorgram
import random
import turtle
from turtle import Turtle, Screen
screen = Screen()
screen.colormode(255)

# Extract 6 colors from an image.
# colors = colorgram.extract('painting.jpg', 30)

# rgb_colors = []
#
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb_colors.append((red, green, blue))
#
# print(rgb_colors)

color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50),
              (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
              (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
              (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
              (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

tom = Turtle()
tom.shape("circle")
tom.speed("fastest")

print(turtle.screensize())

start_y = -200

for _ in range(14):
    tom.hideturtle()
    tom.penup()
    tom.goto(-250, start_y)
    x_cor = tom.xcor()

    while x_cor < 250:
        # tom.fillcolor(random.choice(color_list))
        x_cor = tom.xcor()
        # tom.begin_fill()
        # tom.circle(7)
        # tom.end_fill()
        tom.dot(20, random.choice(color_list))
        tom.forward(40)

    start_y += 30


screen.exitonclick()
