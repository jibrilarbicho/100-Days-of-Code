from turtle import Screen, Turtle

thimy = Turtle()
# thimy.shape("turtle")
thimy.color("red")
# for _ in range(4):
#     thimy.forward(100)
#     thimy.left(90)

for _ in range(15):
    thimy.forward(10)
    thimy.penup()
    thimy.forward(10)
    thimy.pendown()

screen = Screen()
# screen.exitonclick()
