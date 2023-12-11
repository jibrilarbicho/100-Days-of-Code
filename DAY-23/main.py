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
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.moveCar()
    # Detect collision with cars
    for car in car_manager.allCars:
        if car.distance(player) < 20:
            game_is_on = False
screen.exitonclick()
