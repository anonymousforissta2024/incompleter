#Source: https://stackoverflow.com/questions/61945311/i-am-trying-to-perform-the-euler-method-in-python-but-i-am-getting-a-type-error
##Parameters
g = 9.8 #in m/s^2
l = 0.5 #in m
omega0 = np.sqrt(g/l)

def euler(theta0, w0, deltat, t_end):
    t0 = 0 #in s

    ##Constructing the arrays
    t_arr = np.arange(t0, t_end + deltat, deltat)
    w = np.zeros(len(t_arr)) #angular velocity in rad/s
    theta = np.zeros(len(t_arr))

    ##Setting up our initial conditions
    w[0] = w0
    theta = theta0

    ##Performing the Euler method for both small and large angles
    for i in range(len(t_arr) -1):
       w[i + 1] = w[i] - ((omega0)**2)*np.sin(theta[i])*deltat
       theta[i + 1] = theta[i] + w[i]*deltat


    return theta


euler(0.07, 0, 0.05, 5)