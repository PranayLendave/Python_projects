from turtle import TurtleScreen
from snake import Snake


class ScreenCreating(TurtleScreen, Snake):
    def __init__(self):
        super().__init__()
        self.setup(width=self.screen_width, height=self.screen_height)
        self.bgcolor("black")
        self.title("Snake Game")
        self.tracer(0)
