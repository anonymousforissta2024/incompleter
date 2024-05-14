#Source: https://stackoverflow.com/questions/56593409/how-to-solve-attributeerror-module-pandas-has-no-attribute-ewma
expwighted_avg = pd.ewma(ts_log, halflife=12)