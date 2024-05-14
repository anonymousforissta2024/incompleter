#Source: https://stackoverflow.com/questions/68421612/problem-with-udf-in-spark-typeerror-column-object-is-not-callable
from pyspark.sql.functions import udf

punct_remove = udf(lambda s: remove_punct(s))

removeEmoji = udf(lambda s: removeEmoji(s))