from turtle import Screen
from paddle import Paddle
from pongball import Ball
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

l_paddle = Paddle(-425, 0)
r_paddle = Paddle(425, 0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #Detect collison with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collison with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 400 or ball.distance(l_paddle) < 50 and ball.xcor() < -400:
        ball.bounce_x()

    #Missing the ball
    if ball.xcor() > 450 or ball.xcor() < -450:
        ball.reset_position()


screen.exitonclick()
