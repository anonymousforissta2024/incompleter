#Source: https://stackoverflow.com/questions/55720384/typeerror-predict-missing-1-required-positional-argument-params
model = ARIMA(df_mat.Total_Issue_quantities, order=(5,0,0))

y_predict_log = model.predict(start=1, end=24, exog=None, dynamic=False)