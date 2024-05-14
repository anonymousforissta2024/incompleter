#Source: https://stackoverflow.com/questions/60791453/how-can-i-fix-this-typeerror-when-fitting-ode-with-scipy
popt, pcov = optimize.curve_fit(GGM_sol, t, sol.y)