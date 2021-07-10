from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.setheading(135)

    def move(self):
        self.forward(10)
        if self.ycor() > 300:
            self.setheading(self.heading() + 90)
        if self.ycor() < -300:
            self.setheading(self.heading() + 90)
