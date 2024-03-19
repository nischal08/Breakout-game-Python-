from turtle import Turtle, Screen
from ball import Ball
from striker import Striker
from brick import Brick
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()
striker = Striker()
all_brick = []
for i in range(1, 13):
    for j in range(1, 7):
        all_brick.append(Brick(coordinate=(-420 + i * 70, 35 + j * 40)))

screen.listen()
screen.onkeypress(striker.go_left, "Left")
screen.onkeypress(striker.go_right, "Right")
screen.onkeypress(striker.go_left, "a")
screen.onkeypress(striker.go_right, "d")


def collision():
    for brick in all_brick:
        ball_x = ball.xcor()
        ball_y = ball.ycor()
        brick_x = brick.xcor()
        brick_y = brick.ycor()
        distance = abs(ball_x - brick_x) + abs(ball_y - brick_y)
        if distance < 40:
            # Hide the brick
            brick.hideturtle()
            # Remove the brick from the list
            all_brick.remove(brick)
            # Bounce the ball
            ball.bounce_y()


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
        # game_is_on=False
        # scoreboard.r_point()
    collision()
screen.exitonclick()

# TODO:  Detect collision with ball and brick is not stable and going from different direction than it should
