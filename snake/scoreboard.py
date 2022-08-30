from turtle import Turtle
from snake import Snake


class ScoreBoard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, (screen_height//2)-33)
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
        print("score board up")

    def showscore(self):
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
