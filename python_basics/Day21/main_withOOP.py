from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    scoreboard.display()
    ''' Detect colision '''
    if snake.head.distance(food) < 15:
        '''Increase score and display score board'''
        scoreboard.score += 1
        scoreboard.refresh_score()
        snake.single_snake()
        '''After Snake eats food refersh food random location'''
        food.refresh()

        ''' Detect colision with wall'''
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

        '''Detect colision with tail'''
    for segment in snake.all_snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()