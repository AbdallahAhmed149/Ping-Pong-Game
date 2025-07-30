from turtle import Turtle


class Paddles(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 40)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 40)
