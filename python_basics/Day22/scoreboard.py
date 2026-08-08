from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')

class ScoreBoard(Turtle):

    def __init__(self, r_user, l_user):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.r_user = r_user
        self.l_user = l_user
        self.color("white")
        self.penup()
        self.hideturtle()
        '''Always display score board'''
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        '''Right Score board'''
        self.goto(200, 280)
        self.write(f"{self.r_user} Score: {self.r_score}", False, align=ALIGNMENT, font=FONT)
        '''Left Score Board'''
        self.goto(-200, 280)
        self.write(f"{self.l_user} Score: {self.l_score}", False, align=ALIGNMENT, font=FONT)
    
    def point_to_left(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def point_to_right(self):
        self.r_score += 1
        self.update_scoreboard()

