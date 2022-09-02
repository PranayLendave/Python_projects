from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self, screen_width, screen_length):
        super().__init__()
        self.screen_width = screen_width
        self.screen_length = screen_length
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")





    def move(self):
        newx=self.xcor()+10
        newy=self.ycor()+10
        self.goto(newx,newy)

        pass
        # rx = random.randint(-1 * (self.screen_width / 2) + 10, (self.screen_width / 2) - 10)
        # ry = random.randint(-1 * (self.screen_length / 2) + 10, (self.screen_length / 2) - 10)
        # self.goto(rx, ry)

    pass
