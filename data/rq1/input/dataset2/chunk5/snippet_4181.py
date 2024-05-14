#Source: https://stackoverflow.com/questions/45292395/error-typeerror-unorderable-types-int-str
    # I used alias to avoid confusion with the mllib library
from pyparsing import col
from pyspark.ml.clustering import LDA
from pyspark.ml.feature import HashingTF as MLHashingTF, Tokenizer, HashingTF, IDF, StringIndexer
from pyspark.ml.feature import IDF as MLIDF
from pyspark.python.pyspark.shell import sqlContext, sc

from pyspark.sql.types import DoubleType, StructField, StringType, StructType
from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

dbURL = "hdfs://en.wikipedia.org/wiki/Music"
file = sc.textFile("1.txt")
#Define data frame schema
fields = [StructField('key',StringType(),False),StructField('content',StringType(),False)]
schema = StructType(fields)
#Data in format <key>,<listofwords>
file_temp = file.map(lambda l : l.split(","))
file_df = sqlContext.createDataFrame(file_temp, schema)
#Extract TF-IDF From https://spark.apache.org/docs/1.5.2/ml-features.html
tokenizer = Tokenizer(inputCol='content', outputCol='words')
wordsData = tokenizer.transform(file_df)
hashingTF = HashingTF(inputCol='words',outputCol='rawFeatures',numFeatures=1000)
featurizedData = hashingTF.transform(wordsData)
idf = IDF(inputCol='rawFeatures',outputCol='features')
idfModel = idf.fit(featurizedData)
rescaled_data = idfModel.transform(featurizedData)
indexer = StringIndexer(inputCol='key',outputCol='KeyIndex')
indexed_data = indexer.fit(rescaled_data).transform(rescaled_data).drop('key').drop('content').drop('words').drop('rawFeatures')
corpus = indexed_data.select(col("KeyIndex",str).cast("long"), "features").map(list)
model = LDA.train(corpus, k=2)