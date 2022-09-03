from turtle import Turtle
import random
# from snake import Snake


class Food(Turtle):
    def __init__(self, screen_width, screen_length):
        super().__init__()
        self.screen_width = screen_width
        self.screen_length = screen_length
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rx = random.randint(-1 * (self.screen_width / 2) + 15, (self.screen_width / 2) - 15)
        ry = random.randint(-1 * (self.screen_length / 2) + 15, (self.screen_length / 2) - 20)
        self.goto(rx, ry)

    pass
