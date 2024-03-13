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

    # Detect collision with wall vertically
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with wall horizontally
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()


    # Detect collision with striker
    if ball.distance(striker) < 50:
        ball.bounce_y()

screen.exitonclick()


#TODO:  Detect collision with striker is not stable