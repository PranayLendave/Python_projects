from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, screen_width, screen_height):
        self.score = 0
        self.screen_width_1 = screen_width // 2
        self.screen_height_1 = screen_height // 2
        self.left_limit = (-1 * self.screen_width_1) + 10
        self.right_limit = self.screen_width_1 - 10
        self.up_limit = self.screen_width_1 - 40
        self.down_limit = (-1 * self.screen_width_1) + 10

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.addsegment(position)

    def addsegment(self,position):
        i = Turtle(shape="square")
        i.up()
        i.color("white")
        i.goto(position)
        self.segments.append(i)

    def extendsegment(self):
        self.addsegment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            xcor = self.segments[seg_num - 1].xcor()
            ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(xcor, ycor)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(self.screen_width_1*4,self.screen_height_1*4)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]




