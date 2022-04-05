from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def move_left():
    tim.left(20)


def move_right():
    tim.right(20)

def clear():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(key="w", fun=move_right)  #Here screen.onkey is a higher order function as we pass the move_forwards
# function as a input
screen.onkey(key="s", fun=move_left)
screen.onkey(key="d", fun=move_forwards)
screen.onkey(key="a", fun=move_backwards)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
