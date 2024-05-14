#Source: https://stackoverflow.com/questions/75928026/facing-a-typeerror-unsupported-operand-types-for-gurobipy-linexpr-and
# Define the objective function
obj = gp.quicksum(
    gp.quicksum(gp.abs_(pp[i] * x[i, j] - targ) for i in set_I) for j in set_J
) + gp.quicksum(
    gp.quicksum(
        gp.abs_(
            l[i] * x[i, j] / gp.quicksum(x[i, j] for i in set_I) - actual_proportion
        )
        for i in set_I
    )
    for j in set_J
)

model.setObjective(obj, GRB.MINIMIZE)