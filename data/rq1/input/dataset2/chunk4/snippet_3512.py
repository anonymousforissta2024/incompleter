#Source: https://stackoverflow.com/questions/49196607/attributeerror-nonetype-object-has-no-attribute-jvm-when-passing-sql-funct
from pyspark.sql import functions as F

def apply_filter(df, group=F.lit(True)):
    filtered_df = df.filter(group)