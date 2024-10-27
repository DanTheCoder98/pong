import turtle
import paddle

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

right_paddle = paddle.Paddle((350, 0))
left_paddle = paddle.Paddle((-350, 0))

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while True:
    screen.update()
