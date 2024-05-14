#Source: https://stackoverflow.com/questions/69669751/typeerror-bool-object-is-not-subscriptable-with-while-loop
while CheckBlockOrder(dictCon)[1] is not True:
  pair=CheckBlockOrder(dictCon)[0]
  df_shuffle = dictCon[pair[0]]
  df_shuffle = df_shuffle.iloc[np.random.permutation(df_shuffle.index)].reset_index(drop=True)
  dictCon.update({pair[0]:df_shuffle})