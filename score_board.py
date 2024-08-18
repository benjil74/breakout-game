from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 30, 'normal')


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, increase):
        self.score += increase
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def win_game(self):
        self.goto(300, 0)
        self.write("You won !", align=ALIGNMENT, font=FONT)
