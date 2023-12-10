from turtle import Turtle, Screen

import time

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
# paddle = Turtle()

# p
# paddle.goto(350, 0)
scren.listen()
scren.onkey(r_paddle.goup, "Up")
scren.onkey(r_paddle.godown, "Down")
scren.onkey(l_paddle.goup, "w")
scren.onkey(l_paddle.godown, "s")

Gameison = True
while Gameison:
    scren.update()
    time.sleep(0.3)
    ball.move()

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


scren.exitonclick()
