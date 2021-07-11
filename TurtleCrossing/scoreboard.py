from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level: {self.score + 1}", align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
