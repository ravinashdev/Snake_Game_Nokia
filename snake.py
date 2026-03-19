from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
DEFAULT_MOVE_DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270
class Snake:
    # Initialize the Snake object
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    # Internal method to create the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.penup()
            segment.goto(position)
            self.snake.append(segment)
    # Method to keep the snake moving by having each square follow the other
    def auto_move(self):
        for piece_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[piece_num - 1].xcor()
            new_y = self.snake[piece_num - 1].ycor()
            self.snake[piece_num].goto(new_x, new_y)
        self.head.forward(DEFAULT_MOVE_DISTANCE)
    # Directional methods with logic to block it from turning on its own head
    def turn_east(self):
        if self.head.heading() !=WEST:
            self.head.setheading(EAST)
            print("turn east")
    def turn_north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)
            print("turn north")
    def turn_west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)
            print("turn west")
    def turn_south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)
            print("turn south")