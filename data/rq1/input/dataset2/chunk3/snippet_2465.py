#Source: https://stackoverflow.com/questions/53715516/attribute-error-traintype-object-has-no-attribute-v-attribute-should-have
import math

class TrainType(object):
    def __init__(self,t,M,n,L,S,pas):
        self.t = t              # train model
        self.M = M              # train mass [t]
        self.n = n              # numer of axles [-]
        self.L = L              # train length [m]
        self.S = S              # crossection area [m2]
        self.pas = pas          # passenger capacity [-]

# Running resistance force formula
def run_res(self,v):
    C = 0.0035*self.S+0.041*self.L/100+0.002;
    R_L = 9.81*(1.3*math.sqrt(10*self.n/self.M)+0.01*self.v)*self.M+C*v**2
    return R_L

# Power required formula
def power(self,v):
    a = self.run_res(v)
    P = a*v
    return P

train1 = TrainType("Talgo 350",323,21,200,10,318)

print(train1.run_res(10))       # for test reasons v = 10
print(train1.power(10))