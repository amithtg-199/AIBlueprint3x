from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        ''' Here the all_snakes list need to be access throught the class,
        which will be used in move() method aswell, so we need to put self for object to remember it
        '''
        self.all_snakes = []
        self.create_snakes()
        self.head = self.all_snakes[0]

    def create_snakes(self):
        ''' For Local Variables used only once during initialization or inside a method
        we dont need to specify self as object does not need to remember it.
        '''
        x_axis = 0
        y_axis = 0
        for _ in range(0,3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.pensize(20)
            new_segment.penup()
            new_segment.goto(x=x_axis,y=y_axis)
            x_axis -= 20
            self.all_snakes.append(new_segment)

    def move(self):
        for i in range(len(self.all_snakes) -1, 0, -1):
            new_x = self.all_snakes[i - 1].xcor()
            new_y = self.all_snakes[i - 1].ycor()
            self.all_snakes[i].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def single_snake(self):
        single_snake = Turtle("square")
        last_snake = len(self.all_snakes) -1
        single_snake_x = self.all_snakes[last_snake].xcor()
        single_snake_y = self.all_snakes[last_snake].ycor()
        single_snake.color("white")
        single_snake.pensize(20)
        single_snake.penup()
        single_snake.goto(x=single_snake_x,y=single_snake_y)
        self.all_snakes.append(single_snake)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)
    