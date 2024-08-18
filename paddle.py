from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 8)
        self.setpos(position)

    def go_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

