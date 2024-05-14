#Source: https://stackoverflow.com/questions/61384965/attributeerror-str-object-has-no-attribute-name-pyspark
from pyspark.sql import SparkSession
import logging
from pyspark.sql.types import *
from pyspark.sql.functions import to_timestamp
from pyspark.sql.functions import udf
from pyspark.sql.functions import lit
from pyspark.sql.functions import year, month, dayofmonth
from pyspark.context import SparkContext
from pyspark.sql import SQLContext
import argparse

logging.basicConfig(level=logging.INFO,filename = 'parquet.log')
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('--schema_py', '--list', nargs='+', required=True, dest='schema_py', help='Scheam def')

args = parser.parse_args()

schemaField = args.schema_py
print(type(schemaField))   #It will print <class 'list'>

schema = StructType(schemaField) # On this line facing issue
print(type(schema))