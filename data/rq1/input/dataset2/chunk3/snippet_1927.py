#Source: https://stackoverflow.com/questions/53414750/typeerror-line3dcollection-object-is-not-iterable
#Import libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

#Accept input (theta, phi) from a user
print("Put angle theta and phi, 0≤ theta ≤180, 0≤ phi ≤360")
theta = input("theta:")
phi = input("phi:")
theta = np.radians(float(theta))
phi = np.radians(float(phi))

#Calculate x,y,z coordinates
X = np.sin(theta) * np.cos(phi)
Y = np.sin(theta) * np.sin(phi)
Z = np.cos(theta)

#Adjusting the length of an arrow
length = np.sqrt(X**2 + Y**2 + Z**2)
if length > 1:
    X = X/length
    Y = Y/length
    Z = Z/length

# Figure of the animation
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_wireframe(x,y,z, color="black")

# Calculate x,y,z coordinates in the process of the change
length = 9
xgate_theta = np.linspace(theta,theta+np.pi,length)
xgate_phi = np.linspace(phi,phi,length)

#Array of x,y,z coordinates
xgate= []

# Only x coordinates
xgate_x = []

# Only y coordinates
xgate_y = []

# Only z coordinates
xgate_z = []

for i in range(length):
    xgate_x.append(X)
    xgate_z.append(np.cos(xgate_theta[i]))
    xgate_y.append(np.sqrt(1-np.sqrt(xgate_x[i]**2+xgate_z[i]**2))*(-1))
for j in range(length):        
  xgate.append(plt.quiver(0,0,0,xgate_x[j],xgate_y[j],xgate_z[j],color="red"))


ani = animation.ArtistAnimation(fig,xgate,interval=1000)
plt.show()