#Source: https://stackoverflow.com/questions/77336211/typeerror-invalid-rect-assignment-with-vectors
if ball.y == 0 or 480:
    ball.y = vec(random.randint(0, 480), random.randint(0, 480))
if ball.x == 0 or 640:
    ball.x = vec(random.randint(0, 640), random.randint(0, 640))