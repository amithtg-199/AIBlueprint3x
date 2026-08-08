from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0


    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=FONT)

    def display_level(self):
        self.clear()
        self.goto(x=-200, y=250)
        self.write(f"Level: {self.level}", False, align="left", font=FONT)