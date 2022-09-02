from turtle import Turtle


class Paddle():
    def __init__(self):
        self.paddle = Turtle
        self.paddle = Turtle(shape="square")
        self.paddle.shapesize(stretch_wid=3, stretch_len=1,outline=10)
        self.paddle.up()
        self.paddle.color("white")
        self.paddle.goto(0, 0)
