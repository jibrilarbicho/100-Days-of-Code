import random
import turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle


class CarManager:
    def __init__(self):
        self.allCars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        choice = random.randint(1, 6)
        if choice == 1:
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randomy = random.randint(-250, 250)
            newCar.goto(300, randomy)
            self.allCars.append(newCar)

    def moveCar(self):
        for car in self.allCars:
            car.backward(STARTING_MOVE_DISTANCE)

    def levelUp(self):
        self.car_speed += MOVE_INCREMENT
