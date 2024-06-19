import time
from turtle import Screen
from turtle_crossing_player import Player
from turtle_crossing_car_manager import CarManager
from turtle_crossing_scoreboard import Scoreboard

#setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#class instances
score = Scoreboard()
car_manager = CarManager()
player = Player()

#listens for key presses
screen.listen()
screen.onkeypress(player.go_up, "Up")

#game start
game_is_on = True
while game_is_on:
    #screen updation
    time.sleep(0.1)
    screen.update()

    #cars instances
    car_manager.create_car()
    car_manager.move_car()

    #checking for collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #next level if finish line reached
    if player.is_at_finish_line():
        player.go_to_start() #go to start position
        car_manager.level_up_car() #faster cars
        score.increase_level() #increase score

screen.exitonclick()
