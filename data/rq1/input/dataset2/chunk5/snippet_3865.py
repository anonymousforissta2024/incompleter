#Source: https://stackoverflow.com/questions/52372576/typeerror-float-object-is-not-subscriptable-during-scipy-minimize
from numpy import log,sum,var
from numba import njit

@njit
def log_likelihood(params,surg_fx,surg_fx_ses):
    mu_var = params[0]
    exp_var = mu_var + surg_fx_ses**2
    log_lik = -((surg_fx)**2 / (2*exp_var)) - .5*log(exp_var)
    neg_sum_log_lik = -sum(log_lik)
    print(mu_var)
    print(neg_sum_log_lik)
    if np.isnan(neg_sum_log_lik):
        return 1e20
    else:
        return neg_sum_log_lik

@njit
def log_lik_jac(params,surg_fx,surg_fx_ses):
    mu_var = params[0]
    exp_var = mu_var + surg_fx_ses**2
    jc = -sum(((surg_fx)**2 / (2*(exp_var**2))) - (.5/exp_var))
    print(mu_var)
    print(jc)
    return jc

x0 = [np.var(cost_params3)]
shrinkage_est = minimize(log_likelihood,x0,args=(cost_params3,cost_SEs3),jac=log_lik_jac,options={'disp':True},method='BFGS')