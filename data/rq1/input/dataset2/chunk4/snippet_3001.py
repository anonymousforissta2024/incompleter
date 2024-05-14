#Source: https://stackoverflow.com/questions/75928026/facing-a-typeerror-unsupported-operand-types-for-gurobipy-linexpr-and
# Partisan lean (WLOG, lean to a party) of each precinct; binary variable l_i == 1 if the precinct leans towards a party, 0 otherwise
l  = {(i):opt_model.addVar(vtype=gp.GRB.BINARY,
                        name="l_{0}".format(i)) 
for i in set_I}

# Decision variable for n precincts assigned to m districts; binary variable x_i_j == 1 means ith precinct assigned to jth district 
x  = {(i,j):opt_model.addVar(vtype=gp.GRB.BINARY,
                        name="x_{0}_{1}".format(i,j)) 
for i in set_I for j in set_J}

# Population for each of n precincts; integer variable pp_i
pp  ={(i):opt_model.addVar(vtype=gp.GRB.INTEGER,
                        lb=0, 
                        name="pp_{0}".format(i)) 
for i in set_I}

# Target population
V = 9900
targ = math.floor(V // m)

# actual proportion of lean
actual_proportion = gp.quicksum(l[i] for i in set_I)/n