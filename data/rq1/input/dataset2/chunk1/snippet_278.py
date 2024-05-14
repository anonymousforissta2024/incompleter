#Source: https://stackoverflow.com/questions/71682915/pyspark-typeerror-unionbyname-got-an-unexpected-keyword-argument-allowmissi
df =spark.createDataFrame(data,columns)

df1 = spark.createDataFrame([[1, 2, 3]], ["col0", "col1", "col2"])
df2 = spark.createDataFrame([[4, 5, 6]], ["col1", "col2", "col3"])
df1.unionByName(df2, allowMissingColumns=True).show()