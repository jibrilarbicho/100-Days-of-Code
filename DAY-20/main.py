from pickle import FALSE, TRUE
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

gameIsON = TRUE
while gameIsON:
    screnn.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increaseScore()
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() < -280
        or snake.head.ycor() > 280
    ):
        gameIsON = FALSE
        scoreboard.GameOver()


screnn.exitonclick()
