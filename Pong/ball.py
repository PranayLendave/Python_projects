from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self, screen_width, screen_length,speed):
        super().__init__()
        self.xspeed = speed
        self.yspeed = speed
        self.xspeed_1 = self.xspeed
        self.yspeed_1 = self.yspeed
        self.screen_width = screen_width
        self.screen_length = screen_length
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")

    def move(self):
        # # self.yspeed_1=self.yspeed
        # # print(self.ycor())
        # if self.ycor() > 250:
        #     self.yspeed_1 = self.yspeed * -1
        # if self.ycor() < -275:
        #     self.yspeed_1 = self.yspeed
        #
        # if self.xcor() > (self.screen_width//2)-30:
        #     self.xspeed_1 = self.xspeed * -1
        # if self.xcor() < (-self.screen_width//2)+20:
        #     self.xspeed_1 = self.xspeed
        #
        # # print(self.yspeed_1)
        newx = self.xcor() + self.xspeed_1
        newy = self.ycor() + self.yspeed_1
        self.goto(newx, newy)

        pass

    def bounce_x(self):
        self.xspeed_1 = self.xspeed_1 * -1

    def bounce_y(self):
        self.yspeed_1 = self.yspeed_1 * -1

    pass
