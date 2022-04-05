import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race Enter a color :")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_pos = -100
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos)
    y_pos += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print("You won !")
            else:
                print("You loose !")
        rand_distance = random.randint(1, 10)
        turtle.speed("fastest")
        turtle.forward(rand_distance)


screen.exitonclick()
