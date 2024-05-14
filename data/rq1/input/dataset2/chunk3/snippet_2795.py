#Source: https://stackoverflow.com/questions/74253559/python-3-9-caused-typeerror-int-argument-must-be-a-string-a-bytes-like-objec
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
headers = {'User-Agent': agent}
query = requests.get('https://query1.finance.yahoo.com/v7/finance/quote?symbols=AALI.JK')
data = query.json()
data = pd.DataFrame(data['quoteResponse']['result'])
data['regularMarketTime']= pd.to_datetime(data['regularMarketTime'],unit='s').dt.strftime("%Y-%m-%d")
data = data[['regularMarketTime','symbol','regularMarketOpen','regularMarketDayHigh','regularMarketDayLow','regularMarketPrice','regularMarketVolume']]
data_append.append(data)