import turtle


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.x_pos, self.y_pos = position
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.x_pos, self.y_pos)

    def move_up(self):
        y = self.ycor()
        self.sety(y + 20)

    def move_down(self):
        y = self.ycor()
        self.sety(y - 20)
