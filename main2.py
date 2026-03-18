# Linear Version
from turtle import Turtle, Screen
import time
# Initialize Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Nokia")
screen.tracer(0)

starting_positions = [(0,0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    segment = Turtle()
    segment.shape("square")
    segment.penup()
    segment.fillcolor("white")
    segment.setposition(position)
    segments.append(segment)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for segment_num in range(len(segments)-1,0,-1):
        new_x = segments[segment_num-1].xcor()
        new_y = segments[segment_num-1].ycor()
        segments[segment_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].right(90)
    segments[0].forward(20)
screen.exitonclick()