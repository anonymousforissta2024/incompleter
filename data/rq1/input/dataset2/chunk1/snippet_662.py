#Source: https://stackoverflow.com/questions/58073224/typeerror-unhashable-type-numpy-ndarray-on-pivot-table
v2x_pivot = pd.pivot_table(df['2019-07-29':'2019-09-20'],
                           index=['XMStr'],
                           columns=['HasDiscrepency'],
                           values=['V2Xt'],
                           margins=True,
                           aggfunc=[np.mean])