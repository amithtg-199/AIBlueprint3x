from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("Green")
print(timmy.position())
timmy.forward(75)
print(timmy.position())
screen = Screen() # Assigning Screen class to screen object
screen.canvheight=700 # Printing Attribute of screen object

screen.exitonclick() # Accessing the method inside an object

