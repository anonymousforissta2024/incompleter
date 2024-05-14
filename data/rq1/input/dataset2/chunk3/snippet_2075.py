#Source: https://stackoverflow.com/questions/70596596/propagation-in-python-pandas-series-typeerror
joinedDF['combined_error'] = math.sqrt((joinedDF.error1**2 + joinedDF.error2**2).astype(float))