from turtle import Screen
import time
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = ScoreBoard()
ball = Ball()

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "e")
screen.onkey(left_paddle.down, "s")

game_is_on = True
r_bx = False
l_bx = False
while game_is_on:
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	# flag to prevent ball repeatedly calling bounce_x when it hits top/btm edge of paddle.
	if ball.xcor() < 0:
		r_bx = False

	if ball.xcor() > 0:
		l_bx = False

	# collision with top & bottom walls
	if ball.ycor() >= 290 or ball.ycor() < -280:
		ball.bounce_y()

	# collision with right_paddle
	if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
		if not r_bx:
			ball.bounce_x()
			r_bx = True

	# collision with left_paddle
	if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
		if not l_bx:
			ball.bounce_x()
			l_bx = True

	# when right side paddle misses ball
	if ball.xcor() > 380:
		ball.reset_position()
		scoreboard.l_point()

	# when left side paddle misses ball
	if ball.xcor() < -390:
		ball.reset_position()
		scoreboard.r_point()












screen.exitonclick()