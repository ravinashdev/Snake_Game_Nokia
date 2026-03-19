# OOP Version
from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
# Initialize Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Nokia")
screen.tracer(0)

# Initialize Snake Object
snake = Snake()
# Initialize Food Object
food = Food()
# Initialize ScoreBoard Object
score_board = ScoreBoard()
# # Listen for key events to invoke methods to change direction
screen.listen()
screen.onkey(snake.turn_east, "Right")
screen.onkey(snake.turn_north, "Up")
screen.onkey(snake.turn_west, "Left")
screen.onkey(snake.turn_south, "Down")
# Initialize Game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # Initiate snake.auto_move method so snake is not stationary
    snake.auto_move()
    # Write the score_board.write_score() method with the initial conditions
    score_board.write_score()
    # Detect the collision of snake object with food object by measuring its pixel distance
    if snake.head.distance(food) <= 15:
        print("Got it")
        # When collision is detected:
        # Create a new instance of the food object food.new_food() and give it a random position
        food.new_food()
        # Update the score_board object methods score_board.increase_score() and score_board.write_score() so they can display on the screen object
        score_board.increase_score()
        score_board.write_score()
















screen.exitonclick()