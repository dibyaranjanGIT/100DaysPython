from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 275)
        self.color("white")
        self.penup()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def food_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
