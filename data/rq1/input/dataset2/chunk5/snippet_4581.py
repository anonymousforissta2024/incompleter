#Source: https://stackoverflow.com/questions/58025208/attributeerror-float-object-has-no-attribute-append
y = 1/2
b = 1/4


t = []
p = [0,25,43.3013,50,43.3013,25,0,0,0,0,0]

u = []
v = []
p = []
a = []

x = 0.0
for i in range(11):
    a = 0.0 + x
    t.append(a)
    x = x + 0.1

m = 0.45594
k = 18
c = 0.2865

u.append(0)
v.append(0)
p.append(0)

a.append((p[0]-c*v[0]-k*u[0])/m)
dt = 0.1

a.append(m/(b*dt*dt)+y*c/(b*dt))
a.append(m/(b*dt)+(y/b-1)*c)
a.append(((1/(2*b))-1)*m + dt*((y/(2*b))-1)*c)
kn = k + a[1]