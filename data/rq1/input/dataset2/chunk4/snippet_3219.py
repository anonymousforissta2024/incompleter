#Source: https://stackoverflow.com/questions/68942337/typeerror-only-size-1-arrays-can-be-converted-to-python-scalars-with-a-function
x=[0,1,2]
y=np.linspace(69,420,69420)
X, Y = np.meshgrid(x, y)

fig, axs = plt.subplots()
axs.contour(X,Y,G(X,Y),levels=[420.69],colors='black')