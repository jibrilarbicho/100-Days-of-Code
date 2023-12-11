from ast import alias
from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier,24,normal"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")  # this should come before self.write
        self.penup()
        self.goto(0, 270)
        with open("/home/jibril/Documents/Python/DAY-24/data.txt") as data:
            self.HighScore = int(data.read())
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.clear()
        self.write(
            f"Score:{self.score}  HighScore:{self.HighScore}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    def reset(self):
        if self.score > self.HighScore:
            self.highScore = self.score
        with open("/home/jibril/Documents/Python/DAY-24/data.txt", mode="w") as data:
            data.write(f"{self.highScore}")
            self.score = 0

    # def GameOver(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
