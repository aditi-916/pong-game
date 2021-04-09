score_l = 0
score_r = 0
import turtle

win = turtle.Screen()

win.bgcolor("black")
win.title("Pong")
win.setup(height=600, width = 1000)


#Left Paddle
paddle_l = turtle.Turtle()
paddle_l.shape("square")
paddle_l.color("green")
paddle_l.penup()
paddle_l.speed(0)
paddle_l.shapesize(stretch_len=1, stretch_wid=5)
paddle_l.goto(-400, 0)

#Right paddle
paddle_r = turtle.Turtle()
paddle_r.shape("square")
paddle_r.color("green")
paddle_r.penup()
paddle_r.speed(0)
paddle_r.shapesize(stretch_len=1, stretch_wid=5)
paddle_r.goto(400, 0)

#Ball
Ball = turtle.Turtle()
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.speed(0)
Ball.goto(0, 0)
Ball.dx = 2 #change in x
Ball.dy = 2 #change in y

#Pen
pen = turtle.Turtle()
pen.goto(0, 250)
pen.color("white")
pen.penup()
pen.hideturtle()
#Function for left paddle up
def paddle_l_up():
    if paddle_l.ycor() >= 230:
        return
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

#Function for left paddle down
def paddle_l_down():
    if paddle_l.ycor() <= -240:
        return
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

#Function for right paddle up
def paddle_r_up():
    if paddle_r.ycor() >= 230:
        return
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

#Function for right paddle down
def paddle_r_down():
    if paddle_r.ycor() <= -240:
        return
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)

win.listen()
win.onkeypress(paddle_l_up, "w")
win.onkeypress(paddle_l_down, "s")
win.onkeypress(paddle_r_up, "Up")
win.onkeypress(paddle_r_down, "Down")

#Welcome
pen.write("Welcome", align="center", font=("", 24, "bold"))
while True:
    win.update()
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)
    
    if(Ball.ycor() > 290 or Ball.ycor() < -290):
        Ball.dy *= -1    
      
    if(Ball.xcor() > 490):
        Ball.dx *= -1
        score_l += 1
        pen.clear()
        pen.write("Player 1 : {} \t Player 2 : {}".format(score_l, score_r), align="center", font=("", 24, "normal"))
    if(Ball.xcor() < -490):
        Ball.dx *= -1 
        score_r += 1
        pen.clear()
        pen.write("Player 1 : {} \t Player 2 : {}".format(score_l, score_r), align="center", font=("", 24, "normal"))
    if(Ball.xcor() == 380 and Ball.ycor() < paddle_r.ycor() + 50 and Ball.ycor() > paddle_r.ycor() - 50 and Ball.dx > 0):
        Ball.dx *= -1
    if(Ball.xcor() == -380 and Ball.ycor() < paddle_l.ycor() + 50 and Ball.ycor() > paddle_l.ycor() - 50 and Ball.dx < 0):
        Ball.dx *= -1