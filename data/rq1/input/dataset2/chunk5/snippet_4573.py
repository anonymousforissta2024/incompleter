#Source: https://stackoverflow.com/questions/61710648/typeerror-int-object-is-not-subscriptable-while-doing-feature-engineering
# Creation of X1_new
X1_new = []
for x in X1:
    torque = x[0]**2 + x[1]**2 + x[2]**2
    sqr = torque ** 0.5
    X1_new.append(x + [sqr])
print(X1_new[0]) # Look at the first input