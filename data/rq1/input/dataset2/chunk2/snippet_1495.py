#Source: https://stackoverflow.com/questions/51095346/attributeerror-cant-pickle-local-object-op-make-py-thunk-locals-rval-while
log_dose = np.array([-.86, -.3, -.05, .73])
log_dose_shared = shared(log_dose)
n = 5 * np.ones(4, dtype = int)
n_shared = shared(n)
deaths = np.array([0, 1, 3, 5])

with Model() as bioassay_model:
    # Logit model parameters
    alpha = Normal('alpha', 0, sd = 100)
    beta = Normal('beta', 0, sd = 100)
    # Calculate probabilities of death
    theta = invlogit(alpha + beta * log_dose_shared)
    # Data likelihood
    obs_death = Binomial('obs_death', n = n_shared, p = theta, observed = deaths)

with bioassay_model:
    # Obtain starting values via MAP
    start = find_MAP(model = bioassay_model)
    # Instantiate sampler
    step = pm.Metropolis()
    # Draw 2000 posterior samples
    bioassay_trace = sample(50000, step = step, start = start)