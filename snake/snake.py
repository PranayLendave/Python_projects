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
        self.up_limit = self.screen_width_1 - 10
        self.down_limit = (-1 * self.screen_width_1) + 10

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.score = 0
        for index in STARTING_POSITIONS:
            i = Turtle(shape="square")
            i.up()
            i.color("white")
            i.goto(index)
            self.segments.append(i)

    def move(self):
        for seg_num in range(2, 0, -1):
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

    def check(self):
        if self.left_limit > self.head.xcor() or self.head.xcor() > self.right_limit or \
                self.down_limit > self.head.ycor() or self.head.ycor() > self.up_limit:
            print("You have lost")

        else:
            print()

        # if self.head
