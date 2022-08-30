import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race?")
# print(user_bet)
colors=["red","blue","green","yellow","orange","purple"]
y=-70
all_turtle=[]
for index in range(len(colors)):
    i = Turtle(shape="turtle")
    i.up()
    i.color(colors[index])
    i.goto(x=-240,y=y)
    all_turtle.append(i)
    y+=30

print(all_turtle)



if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_turtle=turtle.pencolor()
            if winning_turtle==user_bet:
                print(f"You've won the race with {turtle.pencolor()}")
            else:
                print(f"You've lost the race with {turtle.pencolor()}")
        forward = random.randint(10,20)
        turtle.forward(forward)

