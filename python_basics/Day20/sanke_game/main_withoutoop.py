from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

x_axis = 0
y_axis = 0
all_snakes = []
for s in range(0,3):
    snake = Turtle("square")
    snake.color("white")
    snake.pensize(20)
    snake.penup()
    snake.goto(x=x_axis,y=y_axis)
    x_axis -= 20
    all_snakes.append(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(all_snakes) -1, 0, -1):
        new_x = all_snakes[i - 1].xcor()
        new_y = all_snakes[i - 1].ycor()
        all_snakes[i].goto(new_x, new_y)
    all_snakes[0].fd(20)


















screen.exitonclick()