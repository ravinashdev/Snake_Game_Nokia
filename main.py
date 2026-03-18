# OOP Version
from turtle import Turtle, Screen
from snake import Snake
# Initialize Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Nokia")
snake = Snake()
snake.create_snake()














screen.exitonclick()