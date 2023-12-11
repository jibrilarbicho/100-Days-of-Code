import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.goup, "Up")
game_is_on = True
scoreboard = Scoreboard()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.moveCar()
    # Detect collision with cars
    for car in car_manager.allCars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()
        if player.is_at_finish_line():
            player.GotoStart()
            car_manager.levelUp()
            scoreboard.increase_level()

    # Detecting Succesfful collision
screen.exitonclick()
