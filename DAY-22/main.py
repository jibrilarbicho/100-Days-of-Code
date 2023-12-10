from turtle import Turtle, Screen


scren = Screen()
scren.tracer(0)
scren.setup(800, 600)
scren.title("Pong Game")
scren.bgcolor("black")
from paddle import Paddle
from ball import Ball

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
ball.move
# paddle = Turtle()

# p
# paddle.goto(350, 0)
scren.listen()


Gameison = True
while Gameison:
    scren.update()
    scren.onkey(r_paddle.goup, "Up")
    scren.onkey(r_paddle.godown, "Down")
    scren.onkey(l_paddle.goup, "w")
    scren.onkey(l_paddle.godown, "s")
scren.exitonclick()
