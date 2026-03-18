from turtle import Turtle
class Snake:
    def __init__(self):
        self.starting_positions = [(0,0), (-20, 0), (-40, 0)]
    def create_snake(self):
        snake = []
        for position in self.starting_positions:
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.goto(position)
            segment.color("white")
            snake.append(segment)
        return snake