FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()  # to hide turtle
        self.goto(-280, 250)
        self.updatesCoreboard()

    def updatesCoreboard(self):
        self.clear()
        self.write(f"Level :{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level = +1
        self.updatesCoreboard()

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
