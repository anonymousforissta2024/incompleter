#Source: https://stackoverflow.com/questions/55153695/typeerror-not-supported-between-instances-of-str-and-int-having-this
for file in os.listdir('csv/'):

    filename = 'csv/{}'.format(file)

    print(filename)

    df = pd.read_table(filename,skiprows=3,sep=';')

    df1=df.loc[(df['#timestamp'] <= 0) & (df['#timestamp'] >=-5)]