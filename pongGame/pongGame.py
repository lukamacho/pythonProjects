# This is a sample pong game for beginners.
# You can simply compile it by pycharm and add some extensions like volume

import turtle

WIDTH = 800
HEIGHT = 600
WINNING_SCORE = 2
window = turtle.Screen()
window.title("Pong game by Macho")
window.bgcolor("black")
window.setup(width=WIDTH, height=HEIGHT)
window.tracer(0)


left_score = 0
right_score = 0



#Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=5, stretch_len=1)
left_pad.penup()
left_pad.goto(-350, 0)

#Right paddle

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=5, stretch_len=1)
right_pad.penup()
right_pad.goto(350, 0)


#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2


#Table

table = turtle.Turtle()
table.speed(0)
table.color("white")
table.penup()
table.hideturtle()
table.goto(0, 260)
table.write(f"Player A: {left_score} Player B: {right_score}", align="center", font=("Courier", 24, "normal"))


def increase_speed(dx, dy):
    global  ball
    ball.dx += 0.1
    ball.dy += 0.1
    print(dx)
    print(dy)


#Speed buttons
"""
increase_button = turtle.Turtle()
increase_button.hideturtle()
increase_button.shape("square")
increase_button.color("red")
increase_button.penup()
increase_button.goto(-290, 260)
increase_button.shapesize(stretch_wid=1, stretch_len=3)
increase_button.write("Increase speed", align="center", font=("Courier", 12, "normal"))
increase_button.showturtle()
"""

def left_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def left_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)


def right_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def right_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


window.listen()
window.onkeypress(left_up, "w")
window.onkeypress(left_down, "s")
window.onkeypress(right_down, "Down")
window.onkeypress(right_up, "Up")
while True:
    window.update()
    #increase_button.onclick(increase_speed(ball.dx, ball.dy))

    # ball moving process
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        left_score += 1
        table.clear()
        table.write(f"Player A:{left_score} Player B: {right_score}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        right_score += 1
        table.clear()
        table.write(f"Player A:{left_score} Player B: {right_score}", align="center", font=("Courier", 24, "normal"))

    if left_score == WINNING_SCORE:
        table.clear()
        left_score = 0
        right_score = 0
        ball.goto(0, 0)
        table.write(f"Player A won the game", align="center", font=("Courier", 24, "normal"))
        break

    if right_score == WINNING_SCORE:
        left_score = 0
        right_score = 0
        ball.goto(0, 0)
        table.clear()
        table.write(f"Player B won the game", align="center", font=("Courier", 24, "normal"))
        break
    # Paddle ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor() < right_pad.ycor() + 50 and right_pad.ycor() < ball.ycor() + 50) :
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > - 350)  and (ball.ycor() < left_pad.ycor() + 50 and left_pad.ycor() < ball.ycor() + 50) :
        ball.setx(-340)
        ball.dx *= -1

