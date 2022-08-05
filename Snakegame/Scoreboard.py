from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"score: {self.score}", align="center", font=("Ariel", 24, "normal"))

    def game_over(self):
        self.clear()
        self.write(f"GAME OVER your score: {self.score}", align="center", font=("Ariel", 30, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
