import pandas as pd
df1 = pd.DataFrame(df1, columns=['Name', 'score1', 'score2'])
print('Given Dataframe :\n', df1)
df1['Score_diff'] = df1['score1'] - df1['score2']
print('\nDifference of score1 and score2 :\n', df1)