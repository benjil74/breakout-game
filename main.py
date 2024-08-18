from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from score_board import Score
from bricks import Bricks
import time

screen = Screen()
screen.setup(1600, 800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)
game_is_on = True
paddle = Paddle((0, -360))
ball = Ball()
score_board = Score((0, 350))
color = ["yellow", "green", "orange", "red"]
i = 0
lives = 3
bricks = []
hits = 0
speed_changed = False

for c in color:
    i += 1
    for n in range(0, 20):
        brick = Bricks((-900 + 90 * n, -100 + 50 * i), c)
        bricks.append(brick)

screen.listen()


def move_paddle_with_mouse(event):
    x = event.x - screen.window_width() // 2
    paddle.goto(x, paddle.ycor())


screen.cv.bind('<Motion>', move_paddle_with_mouse)


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    for brick in bricks:
        if ball.distance(brick) < 50:
            ball.bounce()
            brick.goto(2000, 2000)
            bricks.remove(brick)
            hits += 1
            print(hits)
            if brick.color() == ('yellow', 'yellow'):
                score_board.increase_score(1)
            if brick.color() == ('green', 'green'):
                score_board.increase_score(3)
            if brick.color() == ('orange', 'orange'):
                score_board.increase_score(5)
            if brick.color() == ('red', 'red'):
                score_board.increase_score(7)

    if ball.ycor() > 385:
        ball.bounce()
        paddle.shapesize(1, 4)

    if ball.distance(paddle) < 40:
        difference = ball.xcor() - paddle.xcor()
        paddle_width = 100
        if difference < paddle_width / 3:
            ball.x_move = -abs(ball.x_move)
        elif difference > paddle_width / 3:
            ball.x_move = abs(ball.x_move)
        else:
            ball.x_move = ball.x_move
        ball.y_move = abs(ball.y_move)
    if ball.xcor() < -780 or ball.xcor() > 780:
        ball.rebound()
    if ball.ycor() < -380:
        ball.reset_position()
        lives -= 1
        hits = 0
    if hits == 4 and not speed_changed:
        ball.move_speed *= 0.9
        speed_changed = True
    if hits == 12 and speed_changed:
        ball.move_speed *= 0.9
        speed_changed = False
    if lives == 0:
        game_is_on = False
        score_board.game_over()
    if not bricks:
        game_is_on = False

screen.exitonclick()
