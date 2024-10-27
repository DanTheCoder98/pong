import turtle
import paddle

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle_one = paddle.Paddle()

screen.onkey(fun=paddle_one.move_up, key="Up")
screen.onkey(fun=paddle_one.move_down, key="Down")

game_is_on = True
while True:
    screen.update()
