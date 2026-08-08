from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"D:\Python_Udemy_Materials\Python_codes_new\Day24\data.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()

    def display(self):
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}  HighScore: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.display()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(r"D:\Python_Udemy_Materials\Python_codes_new\Day24\data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.display()

