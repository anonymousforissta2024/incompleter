#Source: https://stackoverflow.com/questions/62980036/pyspark-group-by-and-pivot-typeerror
df3=df1.groupby('device_id','date','country','brand').pivot("event_type").count("ad_id")