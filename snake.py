from turtle import Turtle
STARTING_POSITIONS = [(0, -1), (0, 1), (1, 0), (-1, 0)]
DEFAULT_MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.penup()
            segment.goto(position)
            self.snake.append(segment)
    def auto_move(self):
        for piece_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[piece_num - 1].xcor()
            new_y = self.snake[piece_num - 1].ycor()
            self.snake[piece_num].goto(new_x, new_y)
        self.snake[0].forward(DEFAULT_MOVE_DISTANCE)
