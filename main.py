# OOP Version
from turtle import Turtle, Screen
import time
from snake import Snake
# Initialize Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Nokia")
screen.tracer(0)

# Initialize Snake Object
snake = Snake()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.auto_move()















screen.exitonclick()