from turtle import Turtle
MOVE = False
ALIGN = "center"
FONT = ("Courier", 16, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # Set the initial conditions of the score_board Object
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0,270)
        self.hideturtle()
    def write_score(self):
        # Create a message f string as write method can't use an f string
        message = f"Score Board: {self.score}"
        self.write(message, MOVE, ALIGN, FONT)
    def increase_score(self):
        # Increase the score everytime a collision with Food class is detected in main.py
        self.score += 1
        # Clear the screen so new score can get written when it's incremented by 1'
        self.clear()
    def game_over(self):
        self.clear()
        message = f"Game Over! Your final score is: {self.score}"
        self.write(message, MOVE, ALIGN, FONT)