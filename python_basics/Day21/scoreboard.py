from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def display(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.clear()
        self.display()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)

