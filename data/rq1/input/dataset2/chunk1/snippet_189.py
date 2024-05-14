#Source: https://stackoverflow.com/questions/64284524/typeerror-object-of-type-int-has-no-len-in-objective-function-nonlinear-opt
m=GEKKO()
x=m.Var(value=1,lb=0, ub=50)
y=m.Var(value=1, lb=0, ub=50)
m.Equation(puree*x+cutlet*y==1500)
m.Obj(-min(x,y))
m.solve(disp=False)
x.value
y.value