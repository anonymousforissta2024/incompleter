#Source: https://stackoverflow.com/questions/47779351/typeerror-logistic-missing-1-required-positional-argument-params
from scipy.stats import norm

# set up a function to return the log likelihood
def logistic_loglik(params,t,data,sig):
    return sum(norm.logpdf(logistic(params,t),data,sig))

# set standard deviations to be 10% of the population values
sig = ExRatio/10

# parameters for the MCMC
reps = 50000
nparams = 3

# output matrix
par_out = np.ones(shape=(reps,nparams))
# acceptance 
accept = np.zeros(shape=(reps,nparams))
# proposal standard deviations. These have been pre-optimized.
propsigma = [0.05,20,5]

for i in range(1,reps):
    # make a copy of previous parameters
    par_out[i,] = par_out[i-1,]
    for j in range(npars):
        proposed = np.copy(par_out[i,:]) # we need to make a copy so that rejected moves don't affect the original matrix
    proposed[j] = proposed[j] + np.random.normal(0,propsigma[j])
    if (proposed[j]>0): # automatically reject moves if proposed parameter <=0 
        alpha = np.exp(logistic_loglik(proposed,time,ExRatio,sig)-logistic_loglik(par_out[i-1,],time,ExRatio,sig))
        u = np.random.rand()
        if (u < alpha):
            par_out[i,j] = proposed[j]
            accept[i,j] = 1

#print(sum(accept[range(101,reps),:])/(reps-100))


#plt.plot(par_out[:,0])
#plt.plot(par_out[range(101,reps),0])
#plt.plot(par_out[:,0],par_out[:,2])
plt.hist(par_out[range(101,reps),0],50)
print('\n')
a=np.mean(par_out[range(101,reps),0])