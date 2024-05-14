#Source: https://stackoverflow.com/questions/40515418/filter-columns-based-on-a-value-pandas-typeerror-could-not-compare-a-wit
In[44]: df.loc[:, (df != 'a').iloc[0]]