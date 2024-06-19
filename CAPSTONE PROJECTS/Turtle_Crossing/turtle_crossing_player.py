from turtle import Turtle

#characteristics
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    #initialisation
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.lt(90)

    #moving the turtle player upwards
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    #restarting the turtle player to the starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    #going to next level if the turtle player finishes
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
