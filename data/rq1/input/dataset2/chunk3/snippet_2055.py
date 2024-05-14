#Source: https://stackoverflow.com/questions/50773148/typeerror-datetime-on-x-axis-through-matplotlib-animation
import random
import time
from matplotlib import pyplot as plt
from matplotlib import animation
import datetime

# Plot parameters
fig, ax = plt.subplots()
line, = ax.plot([], [], 'k-', label = 'ABNA: Price', color = 'blue')
legend = ax.legend(loc='upper right',frameon=False)
plt.setp(legend.get_texts(), color='grey')
ax.margins(0.05)
ax.grid(True, which='both', color = 'grey')

# Creating data variables
x = []
y = []
x.append(1)
y.append(1)

def init():
    line.set_data(x[:1],y[:1])
    return line,

def animate(args):
    # Args are the incoming value that are animated    
    animate.counter += 1
    i = animate.counter
    win = 60
    imin = min(max(0, i - win), len(x) - win)

    x.append(args[0])
    y.append(args[1])

    xdata = x[imin:i]
    ydata = y[imin:i]

    line.set_data(xdata, ydata)
    line.set_color("red")

    plt.title('ABNA CALCULATIONS', color = 'grey')
    plt.ylabel("Price", color ='grey')
    plt.xlabel("Time", color = 'grey')

    ax.set_facecolor('black')
    ax.xaxis.label.set_color('grey')
    ax.tick_params(axis='x', colors='grey')
    ax.yaxis.label.set_color('grey')
    ax.tick_params(axis='y', colors='grey')

    ax.relim()
    ax.autoscale()

    return line, #line2
animate.counter = 0

def frames1():
    # Generating time variable
    x = 10
    target_time = datetime.datetime.now().strftime("%d %B %Y %H:%M:%000")
    # Extracting time
    FMT = "%d %B %Y %H:%M:%S"
    target_time = datetime.datetime.strptime(target_time, FMT)
    target_time = target_time.time().isoformat()    
    # Converting to time object
    target_time = datetime.datetime.strptime(target_time,'%H:%M:%S') 
    while True:
        # Add new time + 60 seconds
        target_time = target_time + datetime.timedelta(seconds=60)
        x = target_time
        y = random.randint(250,450)/10
        yield (x,y)  
        time.sleep(random.randint(2,5))

anim = animation.FuncAnimation(fig, animate,init_func=init,frames=frames1)

plt.show()