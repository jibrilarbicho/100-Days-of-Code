from pickle import TRUE
from turtle import Screen, Turtle
import time
import turtle

screnn = Screen()
screnn.setup(width=600, height=600)
screnn.bgcolor("black")
screnn.title("My Snake Game")
screnn.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    segment1 = Turtle("square")
    segment1.penup()

    segment1.color("white")
    segment1.goto(position)
    segments.append(segment1)
gameIsON = TRUE
while gameIsON:
    screnn.update()
    time.sleep(0.6)

    for seg in segments:
        seg.forward(20)
screnn.exitonclick()
