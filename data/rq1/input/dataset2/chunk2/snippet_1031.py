#Source: https://stackoverflow.com/questions/52989405/attributeerror-when-scoring-sklearn-pipeline-with-custom-transformer-subclass-bu
model_pipe = Pipeline([('ppp', Pipeline([('rs', RobustScaler()),
                                    ('pcavts', PCAVarThreshSelector(whiten = True))])),
                  ('lin_reg', LinearRegression())])