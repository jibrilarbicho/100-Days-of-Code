from turtle import Screen, Turtle

thimy = Turtle()
thimy.shape("turtle")
thimy.color("red")
for _ in range(4):
    thimy.forward(100)
    thimy.left(90)


screen = Screen()
# screen.exitonclick()
