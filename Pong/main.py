import turtle
from turtle import Turtle, Screen
from paddle import Paddle
import time
from scoreboard import ScoreBoard
from ball import Ball


screen_width = 800
screen_height = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
scoreboard=ScoreBoard(screen_width, screen_height)

paddles=Paddle(screen_width, screen_height,level="medium")
paddles.create_paddles()
ball_1=Ball(screen_width, screen_height)


screen.listen()

screen.onkeypress(paddles.moveup_1, "Up")
screen.onkeypress(paddles.movedown_1, "Down")
screen.onkeypress(paddles.moveup_2, "w")
screen.onkeypress(paddles.movedown_2, "s")










while scoreboard.game_is_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.showscore()
    ball_1.move()
    # snake.check()
    # if snake.head.distance(food) < 15:
    #     scoreboard.score+=1
    #     scoreboard.showscore()qq
    #     food.refresh()
    screen.onkey(scoreboard.working, "?")
    screen.onkey(scoreboard.quit, "q")

# screen.exitonclick()
