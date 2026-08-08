from turtle import Turtle, Screen

tim = Turtle()


def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def anticlockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear_screen():
    tim.reset()



screen = Screen()
screen.listen()
screen.onkeypress(key="a", fun=anticlockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="c", fun=clear_screen)
screen.exitonclick()