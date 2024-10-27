import turtle
import paddle
import ball
import time
import scoreboard

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

right_paddle = paddle.Paddle((350, 0))
left_paddle = paddle.Paddle((-350, 0))
ping_pong = ball.Ball()
score_board = scoreboard.ScoreBoard()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while True:
    time.sleep(0.1)
    screen.update()
    ping_pong.move()

    if ping_pong.ycor() > 280 or ping_pong.ycor() < -280:
        ping_pong.bounce_y()

    if (
        ping_pong.distance(right_paddle) < 50
        and ping_pong.xcor() > 320
        or ping_pong.distance(left_paddle) < 50
        and ping_pong.xcor() < -320
    ):
        ping_pong.x_move()

    if ping_pong.xcor() > 380:
        ping_pong.reset_position()

    if ping_pong.xcor() < -380:
        ping_pong.reset_position()
