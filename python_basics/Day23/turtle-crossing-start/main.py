import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.up)
score.display_level()
loop_counter = 6
game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    '''Here, when the loop enters a sixth iteration each time, then a new core object is created. '''
    loop_counter += 1
    if loop_counter % 6 == 0:
        car.car_manager()
    '''Here we iterate through the car object list and get the car object, and then move each of the car objects in the list.'''
    car.move_cars()

    '''Detect Collision'''
    for single_car in car.all_cars:
        if player.distance(single_car) >=15 and player.distance(single_car) <=23:
            score.game_over()
            game_is_on = False
    
    '''Detect Finish Line'''
    if player.ycor() >= player.finish_line:
        player.restart()
        score.level += 1
        score.display_level()
        car.level_up()

screen.exitonclick()
