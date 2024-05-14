#Source: https://stackoverflow.com/questions/70391782/solve-typeerror-must-be-real-number-not-gk-operators
from gekko import GEKKO
import math

m = GEKKO(remote=False)
x1,x2,lambda1_L,lambda2_L,lambda1_U,lambda2_U,mu1,mu2,mu3,mu4,mu5,mu6,mu7,mu8,W1=[m.Var(1) for i in range(15)] 
sigma_p = math.sqrt(0.028573*x1*x1+0.03129*x2*x2+0.020231*x1*x2)
A= (0.028573*x1+0.010115*x2)/sigma_p
B=(0.03129*x2+0.010115*x1)/sigma_p
m.Equations([292.7182*lambda1_L+(2.25*A-0.025926)*lambda2_L + 446.444*lambda1_U+(2.25*A-0.040535)*lambda2_U-446.444*mu1-0.405858*mu2+(2*A-0.057146*x1-0.020231*x2)*mu3+mu4-mu5+mu6==0,\
            272.9655*lambda1_L+(2.25*B-0.03633)*lambda2_L+513.4587*lambda1_U+(2.25*B-0.051024)*lambda2_U-513.4587*mu1-0.466781*mu2+(2*B-0.06258*x2-0.020231*x1)*mu3+mu4-mu7+mu8==0,\
            mu1*(W1-446.444*x1-513.4587*x2-33)==0,\
            mu2*(0.13-0.405858*x1-0.466781*x2)<=0,\
            mu3*(x1+x2-1)==0,\
            mu5*(0.03-x1)<=0,\
            mu6*(x1-0.38)<=0,\
            mu7*(0.05-x2)<=0,\
            mu8*(x2-0.42)<=0])
m.solve(disp=False)
print(x1.value,x2.value,lambda1_L.value,lambda2_L.value,lambda1_U.value,lambda2_U.value,mu1.value,mu2.value,mu3.value,mu4.value,mu5.value,mu6.value,mu7.value,mu8.value,W1.value)