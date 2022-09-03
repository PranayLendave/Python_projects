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
scoreboard.boundary()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:

    screen.update()
    time.sleep(0.1)

    scoreboard.clear()
    scoreboard.boundary()
    scoreboard.showscore()

    snake.move()
    # snake.check()
    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        snake.extendsegment()
        food.refresh()

    if snake.left_limit > snake.head.xcor() or snake.head.xcor() > snake.right_limit or snake.down_limit > snake.head.ycor() \
            or snake.head.ycor() > snake.up_limit:
        # scoreboard.gameover()
        scoreboard.reset()
        snake.reset()
        food.refresh()


    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            food.refresh()
    #         else:
    #             abc=input("Please enter \"y\" to continue and \"n\" to exit.")
    #             while abc in "yn":
    #                 abc = input("Please enter \"y\" to continue and \"n\" to exit.")
    #                 time.sleep(1)
    #                 pass

print("the end")
screen.exitonclick()
