#Source: https://stackoverflow.com/questions/59686429/pyspark-python3-pickle-picklingerror-could-not-serialize-object-typeerror-ca
udf_call = udf(udf_funct, StringType())
col_columns = [col(c) for c in df.columns]
print(col_columns) 
#has list with bytecodes Column<b' which is not in case of 2.7
udf_call(struct(*col_columns))