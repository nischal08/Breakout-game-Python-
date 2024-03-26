from turtle import Turtle, Screen
from ball import Ball
from striker import Striker
from bricks import Bricks
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

scoreboard = ScoreBoard()
ball = Ball()
striker = Striker()
bricks = Bricks()

bricks.create_bricks()
screen.listen()
screen.onkeypress(striker.go_left, "Left")
screen.onkeypress(striker.go_right, "Right")
screen.onkeypress(striker.go_left, "a")
screen.onkeypress(striker.go_right, "d")


def collision():
    for brick in bricks.all_brick:
        ball_x = ball.xcor()
        ball_y = ball.ycor()
        brick_x = brick.xcor()
        brick_y = brick.ycor()
        distance = abs(ball_x - brick_x) + abs(ball_y - brick_y)
        if distance < 40:
            scoreboard.update_points()
            # Hide the brick
            brick.hideturtle()
            # Remove the brick from the list
            bricks.all_brick.remove(brick)
            # Bounce the ball
            ball.bounce_y()


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall top wall only
    if ball.ycor() > 300:
        ball.bounce_y()

    # Detect collision with wall horizontally
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with striker
    # if ball.ycor() < -200 and (striker.xcor() - 60 < ball.xcor() < striker.xcor() + 60):
    if ball.distance(striker) < 50 and ball.ycor() < -200:
        ball.bounce_y()

    # Detect right ball left
    if ball.ycor() < -280:
        ball.reset_position()
        # game_is_on=False
        scoreboard.reset()
        bricks.create_bricks()
    collision()
screen.exitonclick()

# TODO:  Detect collision with ball and brick is not stable and going from different direction than it should
