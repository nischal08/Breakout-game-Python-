from turtle import Turtle, Screen
from ball import Ball
from striker import Striker
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()
striker = Striker()

screen.listen()
screen.onkeypress(striker.go_left, "Left")
screen.onkeypress(striker.go_right, "Right")
screen.onkeypress(striker.go_left, "a")
screen.onkeypress(striker.go_right, "d")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall top wall only
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with wall horizontally
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with striker
    if ball.distance(striker) < 50 and ball.ycor() < -200:
        ball.bounce_y()

    # Detect right ball left
    if ball.ycor() < -280:
        ball.reset_position()
        # scoreboard.r_point()

screen.exitonclick()

# TODO:  Detect collision with striker is not stable
