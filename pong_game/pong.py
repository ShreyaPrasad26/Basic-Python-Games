import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)  #stops window from updating, speeds up the game

#Paddle a
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1,stretch_wid=6)
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.speed(10)  #speed range 1-10 10 is max. 0 is fastest speed

#Paddle b
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1,stretch_wid=6)
paddle_b.penup()
paddle_b.goto(350,0)
paddle_a.speed(10)

#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.penup()
ball.goto(200,200)
paddle_a.speed(8)

#Ball moves diagonally in screen
ball.dx = 2
ball.dy = 2

point_a = 0
point_b = 0

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.write(f"Player A: {point_a} | Player B: {point_b}",
          align="center",
          font=("Courier",24,"normal"))

#Movement of paddle
def paddle_move_up_a():
    y = paddle_a.ycor()
    if (y<=240):
        y += 20
        paddle_a.sety(y)


def paddle_move_down_a():
    y = paddle_a.ycor()
    if (y>=-240):
        y -= 20
        paddle_a.sety(y)

def paddle_move_up_b():
    y = paddle_b.ycor()
    if (y<=240):
        y += 20
        paddle_b.sety(y)

def paddle_move_down_b():
    y = paddle_b.ycor()
    if (y>=-240):
        y -= 20
        paddle_b.sety(y)

#Binding keys to actions 
wn.listen()
wn.onkeypress(paddle_move_up_a, "w")
wn.onkeypress(paddle_move_down_a, "a")
wn.onkeypress(paddle_move_up_b, "Up")
wn.onkeypress(paddle_move_down_b, "Down")

#Main game loop
while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.dx *= -1
        ball.goto(0,0)
        point_b += 10
        pen.clear()
        pen.write(f"Player A: {point_a} | Player B: {point_b}",
          align="center",
          font=("Courier",24,"normal"))
        
    elif ball.xcor() < -390:
        ball.dx *= -1
        ball.goto(0,0)
        point_a += 10
        pen.clear()
        pen.write(f"Player A: {point_a} | Player B: {point_b}",
          align="center",
          font=("Courier",24,"normal"))

    if (ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
    elif (ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1