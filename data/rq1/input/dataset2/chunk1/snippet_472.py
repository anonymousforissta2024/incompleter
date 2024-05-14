#Source: https://stackoverflow.com/questions/49821328/pyspark-udf-attributeerror-nonetype-object-has-no-attribute-jvm
df.withColumn("myArray", create_users_array(df["myNumber"]))