from turtle import Turtle


class Paddle():
    def __init__(self, screen_width, screen_height, level="easy"):
        self.level = level
        self.screen_width = screen_height
        self.screen_height = screen_height
        self.cal_level()

    def create_paddles(self):

        self.paddle_1 = Turtle(shape="square")
        self.paddle_1.seth(90)
        self.paddle_1.goto(self.screen_width // 2, 0)
        self.paddle_1.shapesize(stretch_wid=0.5, stretch_len=self.paddle_width, outline=10)
        self.paddle_1.up()
        self.paddle_1.color("white")

        self.paddle_2 = Turtle(shape="square")
        self.paddle_2.seth(90)
        self.paddle_2.goto(-(self.screen_width // 2), 0)
        self.paddle_2.shapesize(stretch_wid=0.5, stretch_len=self.paddle_width, outline=10)
        self.paddle_2.up()
        self.paddle_2.color("white")

    def cal_level(self):
        if self.level.lower() == "medium":
            self.paddle_width = 5
        elif self.level.lower() == "hard":
            self.paddle_width = 2
        elif self.level.lower() == "superman":
            self.paddle_width = 1
        else:
            self.paddle_width = 7

    def moveup_1(self):

        self.paddle_1.forward(20)

    def movedown_1(self):

        self.paddle_1.bk(20)

    def moveup_2(self):

        self.paddle_2.forward(20)

    def movedown_2(self):

        self.paddle_2.bk(20)
