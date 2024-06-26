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
            # Hide the brick
            brick.hideturtle()
            # Remove the brick from the list
            bricks.all_brick.remove(brick)
            # Bounce the ball
            ball.bounce_y()
            if brick not in bricks.all_brick:
                scoreboard.update_points()


def check_collision_with_striker():
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    striker_x = striker.xcor()
    striker_y = striker.ycor()
    distance_x = abs(ball_x - striker_x)
    distance_y = abs(ball_y - striker_y)

    if distance_x < 80 and distance_y < 30:
        return True
    else:
        return False


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
    # if ball.distance(striker) < 10:
    #     ball.bounce_y()

    if check_collision_with_striker():
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
# TODO: After Reset ball stop stop and work only after the user press key
# TODO: Game should stop when all bricks are collided and say congratulation player
