#Source: https://stackoverflow.com/questions/64002683/how-to-fix-typeerror-tuple-indices-must-be-integers-or-slices-not-str
from pulp import *
FOODS = ['OATMEAL', 'CHICKEN', 'EGGS', 'MILK']
CUSTOMERS = [1,2,3,4,5]
FACILITY = ['FAC1', 'FAC2', 'FAC3']
dem = {1: 80,      
       2: 270,
       3: 250,
       4: 160,
       5: 180}
maxam = {'FAC1': 500,
         'FAC2': 500,
         'FAC3': 500}
actcost = {'FAC1': 1000,
           'FAC2': 1000,
           'FAC3': 1000}
transp = {'FAC1': {1:4, 2:5, 3:6, 4:8, 5:10},  
          'FAC2': {1:6, 2:4, 3:3, 4:5, 5:8},
          'FAC3': {1:9, 2:7, 3:4, 4:3, 5:4}}

prob = LpProblem("FacilityLocation", LpMinimize) 

use_vars = LpVariable.dicts("UseLocation",FACILITY,0,1,LpBinary)  
serv_vars = LpVariable.dicts("Service", [(i,j) for i in CUSTOMERS 
                                               for j in FACILITY],0)
foods_vars = LpVariable.dicts("food", FOODS, 0)

prob += lpSum(actcost[j]*use_vars[j] for j in FACILITY) + lpSum(transp[j][i]*serv_vars[(i,j)] for j in FACILITY for i in CUSTOMERS)