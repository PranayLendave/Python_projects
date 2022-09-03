from turtle import Turtle
# from snake import Snake
import time


class ScoreBoard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.game_is_on = True
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, (screen_height // 2) - 33)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        print("score board up")

    def showscore(self):
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))

    def disp_msg(self,msg):
        self.clear()
        self.goto(0, 0)
        self.write(f"{msg}", align="center", font=("Arial", 24, "normal"))

    def quit(self):
        print("Thank you for playing")
        self.game_is_on = False

    def working(self):
        self.clear()
        print("The screen is working")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write(f"The screen is working", align="center", font=("Arial", 24, "normal"))
        time.sleep(1)
        self.goto(0, (self.screen_height // 2) - 33)
