import turtle
from turtle import Turtle, Screen
from paddle import Paddle
import time
from scoreboard import ScoreBoard


screen_width = 800
screen_height = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
scoreboard=ScoreBoard(screen_width, screen_height)

paddle_1=Paddle()
screen.listen()











game_is_on = True
while game_is_on:
    pass
    screen.update()
    time.sleep(0.1)
    scoreboard.showscore()
    # snake.move()
    # snake.check()
    # if snake.head.distance(food) < 15:
    #     scoreboard.score+=1
    #     scoreboard.showscore()
    #     food.refresh()
    game_is_on=screen.onkey(scoreboard.quit(), "q")

screen.exitonclick()
