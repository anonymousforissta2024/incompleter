#Source: https://stackoverflow.com/questions/77474231/typeerror-string-indices-must-be-integers-in-pandas-datareader-datareader
company = 'FB'

start = dt.datetime(2012, 1, 1)
end = dt.datetime.now()

data = pdr.DataReader(company, 'yahoo', start, end)