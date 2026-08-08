# from turtle import Turtle, Screen
import turtle as t
from random import choice, randint
timmy_turtle = t.Turtle()
timmy_turtle.shape()
# timmy_turtle.color("red4")

# colour = ['blue', 'crimson', 'gold', 'dark green', 'teal', 'saddle brown']
direction = [0, 90, 180, 270]

## Draw Random shapes ###
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#             timmy_turtle.forward(100)
#             timmy_turtle.right(angle)

# for num_sides in range(3, 11):
#     timmy_turtle.color(choice(colour))
#     draw_shape(num_sides)

### Random Direction Movement###
t.colormode(255) ## Here we are modifying the value of colour mode indie the module
def random_colour():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255) 
    return r, g, b

# def movement():
#     colour_tuple = random_colour()
#     timmy_turtle.pencolor(colour_tuple)
#     path = choice(direction)
#     timmy_turtle.speed(10)
#     timmy_turtle.forward(30)
#     timmy_turtle.setheading(path)


# for i in range(100):
#     timmy_turtle.pensize(10)
#     movement()

timmy_turtle.speed("fastest")
def draw_circle(size):
    for i in range(int(360/size)):
        timmy_turtle.pencolor(random_colour())
        timmy_turtle.circle(100)
        timmy_turtle.setheading(timmy_turtle.heading() + size)

draw_circle(5)

screen = t.Screen()
screen.exitonclick()



