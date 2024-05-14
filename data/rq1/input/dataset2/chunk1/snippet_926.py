#Source: https://stackoverflow.com/questions/55427880/typeerror-unsupported-operand-types-for-map-and-list-with-pyspark
from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler

categoricalColumns = ["workclass", "education", "marital_status", "occupation", "relationship", "race", "sex", "native_country"]
stages = []
for categoricalCol in categoricalColumns:
    #indexing with StringIndexer
    stringIndexer = StringIndexer(inputCol=categoricalCol,
                                 outputCol=categoricalCol+'Index')
    encoder = OneHotEncoder(inputCol=categoricalCol+'Index',
                           outputCol=categoricalCol+'classVec')
    #Add stages
    stages += [stringIndexer, encoder]

# Convert label into label indices using the StringIndexer
label_stringIdx = StringIndexer(inputCol = "income", outputCol = "label")
stages += [label_stringIdx]