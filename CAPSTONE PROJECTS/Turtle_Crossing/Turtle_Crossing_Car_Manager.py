from turtle import Turtle
import random

#characteristics
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

#car manager
class CarManager(Turtle):
    #initialisation
    def __init__(self):
        self.all_cars = [] #list of all cars
        self.car_speed = STARTING_MOVE_DISTANCE

    #creating a car to move horizontaly
    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            y_cood = random.randint(-250,250)
            new_car.goto(300, y_cood)
            self.all_cars.append(new_car)

    #moving the car
    def move_car(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    #leveling up the game
    def level_up_car(self):
        self.car_speed += MOVE_INCREMENT
