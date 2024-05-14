#Source: https://stackoverflow.com/questions/51610133/typeerror-a-float-is-required-pyspark
my_window = Window.partitionBy().orderBy("time")  
gps_d=gps_data.withColumn("dist", dist(
        "longitude", "latitude",
        lag("longitude", 1).over(my_window), lag("latitude", 1).over(my_window)
    ).alias("dist"))