from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.new_x =  10
        self.new_y =  10
        self.sleep_time = 0.1

    def move(self):
        new_x = self.xcor() + self.new_x
        new_y = self.ycor() + self.new_y
        self.goto(x=new_x, y=new_y)

    def rebound_y(self):
        self.new_y *= -1
        if self.sleep_time >= 0.01:
            self.sleep_time -= 0.01

    def rebound_x(self):
        self.new_x *= -1
        if self.sleep_time >= 0.01:
            self.sleep_time -= 0.01

    def refresh(self):
        self.goto(x=0, y=0)
        self.sleep_time = 0.1
        self.new_x *= -1