from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Which Turtle will win, Make your bet", prompt="enter colour 'purple', 'blue', 'green', 'yellow', 'orange or 'red': ")
colors = ["purple" ,"blue", "green", "yellow", "orange", "red"]


def turtles(turtle_name, colour, y_value):
    turtle_name.penup()
    turtle_name.color(colour)
    turtle_name.goto(x=-280, y=y_value)

y_value = -150
all_turtles = []
for colour in colors:
    ''' Multiple Objects of turtle created with same Turtle class it is called as instances of an object '''
    new_turtle = Turtle(shape="turtle") 
    '''This which varies for different objects is called the state of the object instance '''
    turtles(turtle_name=new_turtle, colour=colour, y_value=y_value)
    y_value += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_object in all_turtles:
        distance = random.randint(0,10)
        turtle_object.fd(distance)
        if turtle_object.xcor() > 280:
            if turtle_object.color()[0] == user_bet:
                print(f"Your {user_bet} turtle won the race, Congratulations !!")
            else:
                print(f"{turtle_object.color()[0]} Won, your {user_bet} turtle lost")
            is_race_on = False
            break






screen.exitonclick()