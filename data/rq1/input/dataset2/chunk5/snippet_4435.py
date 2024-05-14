#Source: https://stackoverflow.com/questions/62989992/attribute-error-list-object-has-no-attribute-map
from pyspark.sql.types import *

schemaString="Address_Type,Address_ID,Address_Line_1,Address_Line_2,Address_Line_3,City,County,Zip,State,Country,Dflt_Address_Ind,Row_Insert_TS,Row_Update_TS,SYS_CHANGE_VERSION,SYS_CHANGE_OPERATION"

fields=schemaString.split(",").map(lambda fieldName: StructField(fieldName, StringType(), nullable = true))

schema = StructType(fields)