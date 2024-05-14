#Source: https://stackoverflow.com/questions/73902401/how-to-fix-attribute-error-in-pyomo-model-python
rho = 0.0008
model1 = create_model(rho,R_avg_tolist,Cov_list)

solver = SolverFactory('ipopt')
results = solver.solve(model1, tee = True)