#Source: https://stackoverflow.com/questions/60579185/typeerror-compositemodel-object-is-not-callable-when-trying-to-fit-a-compos
gausmodel = GaussianModel()
linemodel = LinearModel()

params = linemodel.make_params(intercept=40, slope=0)
params += gausmodel.make_params(cen=100, sigma=10, amplitude=100)

model = gausmodel + linemodel

x = pd.DataFrame(np.arange(0, 351), columns=['Pixel Position'])
df = pd.concat([x, intens], axis=1)

# Create models for fitting
peak1 = model(prefix='p1_')
peak2 = model(prefix='p2_')
peak3 = model(prefix='p3_')
peak4 = model(prefix='p4_')

# Set hints for start parameters
params = peak1.make_params()

params['p1_cen'].set(value=80, min=70, max=100)
params['p1_sigma'].set(value=10, min=5, max=20)
params['p1_amplitude'].set(value=80, min=50, max=100000)
params['p1_intercept'].set(value=40, min=30, max=55)
params['p1_slope'].set(value=1, min=0.00001, max=5)

params.update(peak2.make_params())

params['p2_center'].set(value=150, min=140, max=160)
params['p2_sigma'].set(value=10, min=5, max=20)
params['p2_amplitude'].set(value=80, min=50, max=100000)
params['p2_intercept'].set(value=40, min=30, max=55)
params['p2_slope'].set(value=1, min=0.00001, max=5)

params.update(peak3.make_params())

params['p3_center'].set(value=200, min=180, max=220)
params['p3_sigma'].set(value=10, min=5, max=20)
params['p3_amplitude'].set(value=100, min=50, max=100000)
params['p3_intercept'].set(value=40, min=30, max=55)
params['p3_slope'].set(value=1, min=0.00001, max=5)

params.update(peak4.make_params())

params['p4_center'].set(value=250, min=230, max=300)
params['p4_sigma'].set(value=10, min=5, max=20)
params['p4_amplitude'].set(value=100, min=50, max=100000)
params['p4_intercept'].set(value=40, min=30, max=55)
params['p4_slope'].set(value=1, min=0.00001, max=5)

# Define peak model
fit_model = peak1 + peak2 + peak3

# Start fitting
init = fit_model.eval(params, x=df)
result = fit_model.fit(df['Intensity'], params, x=df['Pixel Position'])

print(result.fit_report())