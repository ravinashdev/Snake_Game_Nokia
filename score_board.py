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
        self.high_score = self.retrieve_high_score()
    def write_score(self):
        # Clear the screen so new score can get written when it's incremented by 1'
        self.clear()
        # Create a message f string as write method can't use an f string
        message = f"Score Board: {self.score} High Score: {self.high_score}"
        self.write(message, MOVE, ALIGN, FONT)
    def increase_score(self):
        # Increase the score everytime a collision with Food class is detected in main.py
        self.score += 1
    def reset_score(self):
        # Retrieve high_score from file
        self.high_score = self.retrieve_high_score()
        # Log the high score if the player scores higher than their previous high score
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(self.high_score)
        self.score = 0
    # def game_over(self):
    #     message = f"Game Over!"
    #     self.setposition(0,0)
    #     self.write(message, MOVE, ALIGN, font=("Courier", 32, "bold"))
    # Method to retrieve the high_score from file
    def retrieve_high_score(self):
        with open("high_score.txt", mode="r") as file:
            high_score = int(file.read())
        return high_score
    # Method to write the high_score to the file
    def write_high_score(self,high_score):
        with open("high_score.txt", mode="w") as file:
            file.write(str(high_score))