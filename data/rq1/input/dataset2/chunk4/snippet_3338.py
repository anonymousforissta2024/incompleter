#Source: https://stackoverflow.com/questions/64139685/python-h2o-script-typeerrors-at-end-closing
import h2o
h2o.init()
from h2o.estimators.glm import H2OGeneralizedLinearEstimator
prostate = h2o.import_file("https://h2o-public-test-data.s3.amazonaws.com/smalldata/prostate/prostate.csv")
prostate['CAPSULE'] = prostate['CAPSULE'].asfactor()
prostate['RACE'] = prostate['RACE'].asfactor()
prostate['DCAPS'] = prostate['DCAPS'].asfactor()
prostate['DPROS'] = prostate['DPROS'].asfactor()
predictors = ["AGE", "RACE", "VOL", "GLEASON"]
response_col = "CAPSULE"
glm_model = H2OGeneralizedLinearEstimator(family="binomial", lambda_= 0, compute_p_values=True)
glm_model.train(predictors, response_col, training_frame= prostate)
print('Finished')