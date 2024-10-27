import turtle


class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle(shape="square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(x=350, y=0)

    def move_up(self):
        y = self.paddle.ycor()
        self.paddle.sety(y + 20)

    def move_down(self):
        y = self.paddle.ycor()
        self.paddle.sety(y - 20)
