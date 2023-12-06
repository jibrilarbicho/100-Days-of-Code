from turtle import Screen, Turtle

screnn = Screen()
screnn.setup(width=600, height=600)
screnn.bgcolor("black")
screnn.title("My Snake Game")


starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    segment1 = Turtle("square")
    segment1.color("white")
    segment1.goto(position)

screnn.exitonclick()
