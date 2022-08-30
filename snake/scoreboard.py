from turtle import Turtle
from snake import Snake
ALIGNMENT="center"
FONTNAME="Atari"
THICKNESS=24
class ScoreBoard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, (screen_height // 2) - 33)
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=(FONTNAME, THICKNESS, "normal"))
        self.hideturtle()
        self.screen_width_1 = screen_width // 2
        self.screen_height_1 = screen_height // 2
        self.left_limit = (-1 * self.screen_width_1) +10
        self.right_limit = self.screen_width_1 -10
        self.up_limit = self.screen_width_1 - 30
        self.down_limit = (-1 * self.screen_width_1) + 10

    def boundary(self):
        self.color("white")
        self.pensize(2)
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(self.left_limit,self.down_limit)
        self.pendown()
        self.goto(self.right_limit,self.down_limit)
        self.goto(self.right_limit,self.up_limit)
        self.goto(self.left_limit,self.up_limit)
        self.goto(self.left_limit, self.down_limit)
        self.penup()

        self.goto(0,0)

    def showscore(self):
        self.goto(0,self.up_limit)
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=(FONTNAME, THICKNESS, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=(FONTNAME, THICKNESS+4, "normal"))
        self.goto(0, -20)
        self.write(f"Please enter \"y\" to continue and \"n\" to exit.", align=ALIGNMENT, font=(FONTNAME, THICKNESS -10, "normal"))


