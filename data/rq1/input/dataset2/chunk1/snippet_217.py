#Source: https://stackoverflow.com/questions/69611598/attributeerror-logisticregressiontrainingsummary-object-has-no-attribute-are
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T

spark = SparkSession.builder.getOrCreate()
    
df=spark.read.csv("2018-2010_import.csv",inferSchema=True,header=True)
    
train, test = df.randomSplit([0.7, 0.3], seed=7)
    
print(f"Train set length: {train.count()} records")
print(f"Test set length: {test.count()} records")

train.dtypes

catCols = [x for (x, dataType) in train.dtypes if dataType == "string"]
numCols = [
    x for (x, dataType) in train.dtypes if ((dataType == "double") & (x != "HSCode"))
]

print(numCols)
print(catCols)

train.agg(F.countDistinct("Commodity","Country")).show()

train.groupBy("Commodity","Country").count().show()

from pyspark.ml.feature import (
    OneHotEncoder,
    StringIndexer,
)

string_indexer = [
    StringIndexer(inputCol=x, outputCol=x + "_StringIndexer", handleInvalid="skip")
    for x in catCols
]

one_hot_encoder = [
    OneHotEncoder(
        inputCols=[f"{x}_StringIndexer" for x in catCols],
        outputCols=[f"{x}_OneHotEncoder" for x in catCols],
    )
]

from pyspark.ml.feature import VectorAssembler

assemblerInput = [x for x in numCols]
assemblerInput += [f"{x}_OneHotEncoder" for x in catCols]

vector_assembler = VectorAssembler(
    inputCols=assemblerInput, outputCol="VectorAssembler_features", handleInvalid="skip"
)

stages = []
stages += string_indexer
stages += one_hot_encoder
stages += [vector_assembler]

from pyspark.ml import Pipeline

pipeline = Pipeline().setStages(stages)
model = pipeline.fit(train)

pp_df = model.transform(test)

pp_df.select(
    "HSCode", "Commodity", "value", "Country", "VectorAssembler_features",
).show(truncate=False)
from pyspark.ml.classification import LogisticRegression

data = pp_df.select(
    F.col("VectorAssembler_features").alias("features"),
    F.col("HSCode").alias("label"),
)

model = LogisticRegression().fit(data)

model_summary.areaUnderROC