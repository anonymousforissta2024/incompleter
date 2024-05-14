#Source: https://stackoverflow.com/questions/50104197/pandas-erratically-returning-typeerror-cannot-do-slice-indexing-on-class-panda
col_names = ['Col_' + str(i) for i in range(1, max_col_nr)]

df = pd.read_csv(myFile, sep = '\t', names = col_names)
df2 = df.set_index("Col_2", drop = False)
df3 = (df2.loc[310:400,"Col_4"])
US_Av = (int(round(df4.mean())))