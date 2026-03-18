# Linear Version
from turtle import Turtle, Screen

# Initialize Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Nokia")

starting_positions = [(0,0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    segment = Turtle()
    segment.shape("square")
    segment.penup()
    segment.fillcolor("white")
    segment.setposition(position)
    segments.append(segment)

for segment in segments:
    segment.forward(10)

screen.exitonclick()