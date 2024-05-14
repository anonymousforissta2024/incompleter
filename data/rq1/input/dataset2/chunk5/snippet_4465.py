#Source: https://stackoverflow.com/questions/54514394/typeerror-normalize-argument-2-must-be-str-not-series-with-a-dataframe-of-st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import unicodedata
sid = SentimentIntensityAnalyzer()
for date, row in df_news.T.iteritems():
    try:
        sentence = unicodedata.normalize('NFKD', df_news.loc[date, 'name']).encode('ascii','ignore')
        #print((sentence))
        ss = sid.polarity_scores(str(sentence))
        df_news.set_value(date, 'compound', ss['compound'])
        df_news.set_value(date, 'neg', ss['neg'])
        df_news.set_value(date, 'neu', ss['neu'])
        df_news.set_value(date, 'pos', ss['pos'])
    except TypeError:
        print(df_news.loc[date, 'name'])
        print(date)