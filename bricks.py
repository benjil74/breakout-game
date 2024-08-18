from turtle import Turtle


class Bricks(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("square")
        self.shapesize(2, 4)
        self.setpos(position)

