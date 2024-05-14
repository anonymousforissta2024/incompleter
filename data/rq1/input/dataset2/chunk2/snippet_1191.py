#Source: https://stackoverflow.com/questions/62878497/how-to-solve-attributeerror-list-object-has-no-attribute-lower-in-scipy-mini
from scipy.optimize import minimize

def f(Y,t,params):
    r, p, K, alpha = params
    return r * (Y ** p) * (1 - (Y / K) ** alpha)

t = np.linspace(0, len(df), len(df))
y0=1
initial_guess = [0.5, 0.5, 200000,0.7]

# result = minimize(f,initial_guess) #I used this one first but I got an error (TypeError: f() missing 2 required positional arguments: 't' and 'params') so I changed this one to the one below (I added y0 and t)

result = minimize(f, y0,t,initial_guess)