#Source: https://stackoverflow.com/questions/62732790/apply-a-function-to-columns-in-pandas-raises-attributeerror
def _replace_datetime_with_datetime_pub(news_dataframe):
    news_dataframe.dateTime = np.where(news_dataframe.dateTimePub, news_dataframe.dateTimePub, news_dataframe.dateTime)
    return pd.to_datetime(news_dataframe.dateTime)

df.apply(_replace_datetime_with_datetime_pub) 