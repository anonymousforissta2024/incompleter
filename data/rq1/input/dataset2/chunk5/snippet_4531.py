#Source: https://stackoverflow.com/questions/67255437/typeerror-not-supported-between-instances-of-method-and-int-but-in-thi
while True:
    wn.update()  
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy)

    # Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1