from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.goto(-100, 150)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 150)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.lscore += 1
        self.updateScoreBoard()

    def r_point(self):
        self.rscore += 1
        self.updateScoreBoard()
