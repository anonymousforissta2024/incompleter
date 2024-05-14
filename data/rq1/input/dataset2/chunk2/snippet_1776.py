#Source: https://stackoverflow.com/questions/76359431/typeerror-in-django-float-argument-must-be-a-string-or-a-number-not-tuple
ticker = yf.Ticker(symbols[pk])
price_arr = ticker.history(period='1d')['Close']
price = np.array(price_arr)[0]