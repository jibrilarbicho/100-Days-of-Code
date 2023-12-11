# from pickle import FALSE, TRUE
from turtle import Screen, Turtle

from scoreboard import Scoreboard

from food import Food
from snake import Snake
import time
import turtle

snake = Snake()
food = Food()
screnn = Screen()
scoreboard = Scoreboard()
screnn.setup(width=600, height=600)
screnn.bgcolor("black")
screnn.title("My Snake Game")
screnn.tracer(0)
screnn.listen()
screnn.onkey(snake.Up, "Up")
screnn.onkey(snake.Down, "Down")
screnn.onkey(snake.Left, "Left")
screnn.onkey(snake.Right, "Right")

gameIsON = True
while gameIsON:
    screnn.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() < -280
        or snake.head.ycor() > 280
    ):
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screnn.exitonclick()
