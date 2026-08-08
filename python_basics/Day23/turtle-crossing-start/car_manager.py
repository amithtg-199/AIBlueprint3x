from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_LENGTH = 1
CAR_WIDTH = 2

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def car_manager(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=CAR_WIDTH, stretch_len=CAR_LENGTH)
        new_car.penup()
        new_car.seth(180)
        y_axis = random.randint(-248, 248)
        new_car.goto(x=300, y=y_axis)
        '''Each time a new object is created It will be stored in the list.'''
        self.all_cars.append(new_car)
    
    def move_cars(self):
        '''From the list, we are going to take each object and perform the operations over that object.'''
        for car in self.all_cars:
            car.fd(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



