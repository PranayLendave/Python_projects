import turtle
from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard
from screen import ScreenCreating

screen_width = 600
screen_height = 600

# screen = ScreenCreating()

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(screen_width, screen_height)
food = Food(screen_width, screen_height)
scoreboard = ScoreBoard(screen_width, screen_height)

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.check()
    if snake.head.distance(food) < 15:
        scoreboard.score+=1
        scoreboard.showscore()
        food.refresh()

screen.exitonclick()
