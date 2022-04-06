from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Chase")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.2)
    snake.move()

    if snake.segments[0].distance(food) < 10:
        food.refresh()
        score.food_score()
        snake.extend()

    for segment in snake.segments:
        print(snake.segments[0].distance(segment))
        if segment == snake.segments[0]:
            print('z')
            pass
        elif snake.segments[0].distance(segment) < 10:
            print(f"End {snake.segments[0].distance(segment)}")
            game_is_on = False
            score.game_over()

screen.exitonclick()
