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
scoreboard = ScoreBoard(screen_width, screen_height)

paddles = Paddle(screen_width, screen_height, level="medium")
paddles.create_paddles()
ball_1 = Ball(screen_width, screen_height,speed=10)

screen.listen()

screen.onkeypress(paddles.moveup_1, "Up")
screen.onkeypress(paddles.movedown_1, "Down")
screen.onkeypress(paddles.moveup_2, "w")
screen.onkeypress(paddles.movedown_2, "s")

while scoreboard.game_is_on:
    screen.update()
    time.sleep(0.1)

    scoreboard.showscore()
    scoreboard.draw_ractangle()
    ball_1.move()
    if ball_1.ycor() > screen_height // 2 - 50 or ball_1.ycor() < -(screen_height // 2 - 25):
        ball_1.bounce_y()

    if ball_1.xcor() == screen_width // 2 - 120 or ball_1.xcor() == -(screen_width // 2 - 120):
        if ball_1.distance(paddles.paddle_1) < paddles.paddle_width*10 or ball_1.distance(paddles.paddle_2)<paddles.paddle_width*10:
            ball_1.bounce_x()
    # snake.check()
    # if snake.head.distance(food) < 15:
    #     scoreboard.score+=1
    #     scoreboard.showscore()qq
    #     food.refresh()
    screen.onkey(scoreboard.working, "?")
    screen.onkey(scoreboard.quit, "q")
    if ball_1.xcor() > screen_width // 2 or ball_1.xcor() < -(screen_width // 2 ):
        scoreboard.disp_msg("Game Over")
        scoreboard.quit()

screen.exitonclick()
