#Source: https://stackoverflow.com/questions/74798015/typeerror-structtype-can-not-accept-object-1-1-2021-10000-am-in-type
from pyspark.sql.functions import to_timestamp
from pyspark.sql.types import StringType, StructType, StructField

schema = StructType([
    StructField("timestamp_str", StringType(), True)
])

data = [("1/1/2021 1:00:00 AM")]
df = spark.createDataFrame(data, schema=schema)

df = df.withColumn("timestamp", to_timestamp("timestamp_str", "MM/dd/yyyy hh:mm:ss a"))