from turtle import Turtle

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
        self.write(message, move=False, align="center", font=("Courier", 16, "bold"))
    def increase_score(self):
        # Increase the score everytime a collision with Food class is detected in main.py
        self.score += 1
        # Clear the screen so new score can get written when it's incremented by 1'
        self.clear()