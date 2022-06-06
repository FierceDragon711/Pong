from turtle import Turtle, Screen
from players import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

l_paddle = Paddle((-390,0))
r_paddle = Paddle((390,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(key="Up", fun= r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)
screen.onkeypress(key="w", fun= l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    scoreboard
    ball.move()
    if (ball.distance(r_paddle) < 54 and ball.xcor() > 370) or (ball.distance(l_paddle) < 54 and ball.xcor() < -370):
        ball.bounce_x()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 380:
        ball.miss()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.miss()
        scoreboard.r_point()
screen.exitonclick()
