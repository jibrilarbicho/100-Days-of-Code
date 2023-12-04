from turtle import Screen, Turtle
import random
import turtle

thimy = Turtle()
# thimy.shape("turtle")
thimy.color("red")
# for _ in range(4):
#     thimy.forward(100)
#     thimy.left(90)

# for _ in range(15):
#     thimy.forward(10)
#     thimy.penup()
#     thimy.forward(10)
#     thimy.pendown()

# screen = Screen()
# # screen.exitonclick()

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "gray",
    "cyan",
]
direction = [0, 90, 180, 270]

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         thimy.forward(100)
#         thimy.right(angle)


# for shape_side in range(3, 12):
#     thimy.color(random.choice(colors))
#     draw_shape(shape_side)
thimy.pensize(15)
thimy.speed(1)
for _ in range(200):
    thimy.color(random.choice(colors))
    thimy.forward(30)
    thimy.setheading(random.choice(direction))
