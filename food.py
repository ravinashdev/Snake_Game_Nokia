from turtle import Turtle
import random
# Class Turtle is the parent Class of Food
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed(0)
        self.new_food()
    def new_food(self):
        random_x_coordinate = random.randint(-280, 280)
        random_y_coordinate = random.randint(-280, 280)
        self.setposition(random_x_coordinate, random_y_coordinate)
