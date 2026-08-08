from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
PADDLE_RIGHT = (365, 0)
PADDLE_LEFT = (-365, 0)
LEFT_USER = input("What is first player name: ").strip().title()
RIGHT_USER = input("What is second player name: ").strip().title()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Ping Pong Game")
screen.tracer(0)
screen.listen()

paddle_right = Paddle(PADDLE_RIGHT)
paddle_left = Paddle(PADDLE_LEFT)
scoreboard = ScoreBoard(r_user=RIGHT_USER, l_user=LEFT_USER)
ball = Ball()

screen.onkeypress(key="Up", fun=paddle_right.up)
screen.onkeypress(key="Down", fun=paddle_right.down)
screen.onkeypress(key="w", fun=paddle_left.up)
screen.onkeypress(key="s", fun=paddle_left.down)

is_game_on = True
while is_game_on:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()
    '''Detect Wall Collision'''
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.rebound_y()

    '''Detect ball collision with right paddle'''
    if ball.distance(paddle_right) < 55 and ball.xcor() > 330:
            ball.rebound_x()

    '''Detech Ball collision with left paddle'''
    if ball.distance(paddle_left) < 55 and ball.xcor() < -330:
            ball.rebound_x()

    '''Ball misses the Right paddle and increase y-score'''
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.point_to_left()

    '''Ball Misses the left Paddle and increase x-score'''
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.point_to_right()















screen.exitonclick()