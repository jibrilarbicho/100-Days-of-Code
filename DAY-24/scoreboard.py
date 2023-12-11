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
        self.updateScoreboard()
        self.hideturtle()
        self.highScore = 0

    def updateScoreboard(self):
        self.clear()
        self.write(
            f"Score:{self.score}  HighScore:{self.highScore}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            self.score = 0

    # def GameOver(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
