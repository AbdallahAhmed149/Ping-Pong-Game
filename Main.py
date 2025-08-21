from turtle import Screen
from Brackets import Paddles
from Ball import Ball
from Score import Scoreboard
import time

window = Screen()
window.title("Welcome to the PingPong Game!")
window.bgcolor("black")
window.setup(width=1000, height=700)
window.tracer(0)

# Scoreboard
board1 = Scoreboard()
score1 = 0
board1.goto(100, 250)
board1.write(f"{score1}", font=("bold", 50, "normal"))

board2 = Scoreboard()
score2 = 0
board2.goto(-100, 250)
board2.write(f"{score2}", font=("bold", 50, "normal"))

# Paddle_1
paddle1 = Paddles()
paddle1.goto(470, 0)
window.listen()
window.onkey(paddle1.move_up, "Up")
window.onkey(paddle1.move_down, "Down")

# Paddle_2
paddle2 = Paddles()
paddle2.goto(-470, 0)
window.onkey(paddle2.move_up, "w")
window.onkey(paddle2.move_down, "s")

ball = Ball()
speed = 0.1

game_on = True
while game_on:
    window.update()
    time.sleep(speed)
    ball.goto(ball.xcor() + ball.move_x, ball.ycor() + ball.move_y)

    if ball.ycor() >= 340 or ball.ycor() <= -340:
        ball.move_y *= -1

    if (ball.xcor() >= 450 and ball.distance(paddle1) <= 50) or (
        ball.xcor() <= -450 and ball.distance(paddle2) <= 50
    ):
        ball.move_x *= -1

    if ball.xcor() > 510:
        score2 += 1
        board2.clear()
        board2.write(f"{score2}", font=("bold", 50, "normal"))
        speed *= 0.5
        ball.goto(0, 0)
        ball.move_x *= -1

    if ball.xcor() < -510:
        score1 += 1
        board1.clear()
        board1.write(f"{score1}", font=("bold", 50, "normal"))
        speed *= 0.5
        ball.goto(0, 0)
        ball.move_x *= -1

    if score1 == 10:
        game_on = False
        window.clear()
        window.bgcolor("red")
        board1.goto(0, 0)
        board1.write(
            "*******Player_1 WIN*******", font=("bold", 50, "italic"), align="center"
        )

    if score2 == 10:
        game_on = False
        window.clear()
        window.bgcolor("blue")
        board2.goto(0, 0)
        board2.write(
            "*******Player_2 WIN*******", font=("bold", 50, "italic"), align="center"
        )

window.exitonclick()
