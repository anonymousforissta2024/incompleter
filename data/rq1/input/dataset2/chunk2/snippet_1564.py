#Source: https://stackoverflow.com/questions/45117616/newton-optimize-typeerror-float-object-is-not-subscriptable
from scipy import optimize

#########################
# IR Fixed PV Valuation #
#########################

def IR_Fixed_Valuation_PV(ValDate, Notional_v, AccrualDays_v, rate, Df_v):
    PV=[]  
    for i in range(0,len(AccrualDays_v)): 
        if sum(AccrualDays_v[0:i+1])<ValDate:
            if i==0:
                PV.append(0)
            else:
                PV.append(PV[-1])
        else:
            PV.append(Notional_v[i]*((1+rate)**AccrualDays_v[i]-1)*Df_v[i])
    return (PV)

#############################
# IR Float Leg Valuation PV #
#############################

def IR_Float_Valuation_PV(ValDate, Notional_v, AccrualDays_v, Fra_rate_v, rate1, rate2, Df_v):

    PV=[]  
    for i in range(0,len(Notional_v)): 
        if sum(AccrualDays_v[0:i+1])<ValDate:
            if i==0:
                PV.append(0)
            else:
                PV.append(PV[-1])
        else:
            PV.append(Notional_v[i]*(((((1+Fra_rate_v[i])**(1/252)-1)*rate1+1)*(1+rate2)**(1/252))**(252*AccrualDays_v[i])-1)*Df_v[i])
    return (PV)


def fun(a, b, c, d, e, f, g, h, i, j):
    return sum(IR_Fixed_Valuation_PV(0, a, b, c, d)) - sum(IR_Float_Valuation_PV(0, e, f, g, h,i,j))

#def main():
a=[1e+06,1e+06,1e+06]
b=[0.33,0.33,0.33]
c=0.10
d=[0.97, 0.96, 0.92]

e=a
f=b
g=[0.09,0.11,0.12]
h=1
i=0
j=d
res = optimize.newton(fun, c, args=(a,b,d,e,f,g,h,i,j,),tol=10e1, maxiter=50)