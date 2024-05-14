#Source: https://stackoverflow.com/questions/69054414/why-am-i-getting-a-filenotfounderror-when-trying-to-create-a-sparkcontext
import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":
    sc = SparkContext(appName="PythonStreamingReceiverKafkaWordCount")