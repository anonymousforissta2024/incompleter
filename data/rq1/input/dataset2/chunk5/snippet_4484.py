#Source: https://stackoverflow.com/questions/54514394/typeerror-normalize-argument-2-must-be-str-not-series-with-a-dataframe-of-st
doc_data = {
  "size": 10,
  "query": {
    "bool": {
      "must" : [
       {"term":{"text":"gucci"}}
     ]
    }
  }
 }

docs = create_doc("https://elastic:rKzWu2WbXI@db.luxurynsight.com/luxurynsight_v2/news/_search",doc_data)


information_df = pd.DataFrame.from_dict(docs.json()["hits"]["hits"])

# Reading the JSON file
df_news = pd.read_json('data.json')

# Converting the element wise _source feature datatype to dictionary
df_news._source = df_news._source.apply(lambda x: dict(x))

# Creating name column
df_news['name'] = df_news._source.apply(lambda x: x['name'])

# Creating createdAt column
df_news['createdAt'] = df_news._source.apply(lambda x: x['createdAt'])

df_news['createdAt'] =  pd.to_datetime(df_news['createdAt'], unit='ms')

df_news['createdAt'] = pd.DatetimeIndex(df_news.createdAt).normalize()
#df_news.createdAt.dt.normalize()

df_news['Date'] = df_news['createdAt']

df_news = df_news[['name','Date']]
df_news = df_news.set_index('Date')
information_df._source = information_df.apply(lambda x: dict(x))
df_news.reset_index()