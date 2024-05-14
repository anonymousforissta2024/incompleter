#Source: https://stackoverflow.com/questions/74524141/matplotlib-attributeerror-nonetype-object-has-no-attribute-get-view
import numpy as np
from numpy import sqrt
from random import randint
import math
from matplotlib import pyplot as plt
from matplotlib import collections
plt.rcParams["figure.figsize"] = 4, 4
from matplotlib.animation import FuncAnimation

np_rnd = np.random.default_rng()


class Ball:
    x0 = 0
    y0 = 0
    x = 0
    y = 0
    r = 0
    t = 0
    m = 0
    v_speed = np.array([0, 0])
    v_accel = np.array([0, 0])

    def __init__(self, x_, y_, r_, m_, v_speed_, v_accel_):
        self.m = m_
        self.x = x_
        self.y = y_
        self.x0 = x_
        self.y0 = y_
        self.r = r_
        self.v_speed = v_speed_
        self.v_accel = v_accel_
        self.t = 0


def get_cmap(n, name='hsv'):
    return plt.cm.get_cmap(name, n)


FPS = 77

X_MIN = -1
X_MAX = 100

Y_MIN = -1
Y_MAX = 100


RADIUS_MIN = 1
RADIUS_MAX = 3

K_RADIUS = 50
MASS_MAX = 6

SPEED_MAX = 0.5
ACCEL_MAX = 0

N = 5
T = 1


ball_list = []
xy_balls = np.c_[np_rnd.integers(X_MIN+RADIUS_MAX, X_MAX-RADIUS_MAX,(N)),
                 np_rnd.integers(Y_MIN+RADIUS_MAX, Y_MAX-RADIUS_MAX,(N))]

r_balls = np_rnd.integers(RADIUS_MIN, RADIUS_MAX, N)
color_balls = np.arange(0, N)




fig, ax = plt.subplots()
ax.plot([X_MIN, X_MAX], [0, 0], color='black', linewidth=0.5)
plt.annotate("x", xy=(X_MAX - 2, 0))
ax.plot([0, 0], [Y_MIN, Y_MAX], color='black', linewidth=0.5)
plt.annotate("y", xy=(0, Y_MAX - 2))
plt.annotate("0", xy=(2, 2))
cmap = get_cmap(N)
for i in range(N):
    ball_list.append(Ball(xy_balls[i][0],
                          xy_balls[i][1],
                          r_balls[i],
                          randint(1, MASS_MAX),
                          np_rnd.uniform(0, SPEED_MAX, size=2),
                          np_rnd.uniform(0, ACCEL_MAX, size=2)
                          )
                     )

balls_plt = [plt.Circle(center, radius=radius, color=cmap(color)) for center, radius, color in zip(xy_balls, r_balls, color_balls)]

balls_plt_updater = balls_plt



def checkBorder(ball):
    if (ball.x > X_MAX) or (ball.x < X_MIN):
        ball.x = (X_MAX - 1) if ball.x > X_MAX else X_MIN + 1
        ball.x0 = ball.x
        ball.y0 = ball.y
        ball.v_speed[0] = -(ball.v_speed[0] + ball.t * ball.v_accel[0])
        ball.v_speed[1] = ball.v_speed[1] + ball.t * ball.v_accel[1]
        ball.v_accel[0] = -ball.v_accel[0]
        ball.t = 0

    if (ball.y > Y_MAX) or (ball.y < Y_MIN):
        ball.y = (Y_MAX - 1) if ball.y > Y_MAX else Y_MIN + 1
        ball.x0 = ball.x
        ball.y0 = ball.y
        ball.v_speed[0] = ball.v_speed[0] + ball.t * ball.v_accel[0]
        ball.v_speed[1] = -(ball.v_speed[1] + ball.t * ball.v_accel[1])
        ball.v_accel[1] = -ball.v_accel[1]
        ball.t = 0


def checkBite(ball1, ball2):
    D = math.sqrt(((ball1.x - ball2.x) ** 2) + ((ball1.y - ball2.y) ** 2))

    if D < (ball1.r + ball2.r):
        ball1.v_speed[0] = ((ball1.m - ball2.m) * ball1.v_speed[0] + 2 * ball2.m * ball2.v_speed[0]) / (
                    ball1.m + ball2.m)
        ball1.v_speed[1] = ((ball1.m - ball2.m) * ball1.v_speed[1] + 2 * ball2.m * ball2.v_speed[1]) / (
                    ball1.m + ball2.m)
        ball2.v_speed[0] = ((ball2.m - ball1.m) * ball2.v_speed[0] + 2 * ball1.m * ball1.v_speed[0]) / (
                    ball1.m + ball2.m)
        ball2.v_speed[1] = ((ball2.m - ball1.m) * ball2.v_speed[1] + 2 * ball1.m * ball1.v_speed[1]) / (
                    ball1.m + ball2.m)

        ball1.x0 = ball1.x + (ball1.v_speed[0] * ball1.r)
        ball1.y0 = ball1.y + (ball1.v_speed[1] * ball1.r)
        ball2.x0 = ball2.x + (ball2.v_speed[0] * ball2.r)
        ball2.y0 = ball2.y + (ball2.v_speed[1] * ball2.r)
        ball1.t = T
        ball2.t = T



def setCoord(ball):
    ball.x = ball.x0 + ball.v_speed[0] * ball.t + (ball.v_accel[0] * (ball.t ** 2)) / 2
    ball.y = ball.y0 + ball.v_speed[1] * ball.t + (ball.v_accel[1] * (ball.t ** 2)) / 2
    ball.t += T



def animate(i, balls):
    for j in range(len(balls)):
        #for k in range(j+1, len(balls)):
        #    checkBite(balls[j], balls[k])
        checkBorder(balls[j])
        setCoord(balls[j])
        balls_plt[j].center = balls[j].x, balls[j].y


    return balls_plt_updater


anim = FuncAnimation(fig=fig, func=animate, fargs=(ball_list,),
                     frames=np.linspace(0, FPS * 2, num=1000, dtype=np.intc, endpoint=False),
                     interval=1000 / (FPS), blit=True, repeat=True)

plt.show()