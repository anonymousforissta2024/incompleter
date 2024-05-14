#Source: https://stackoverflow.com/questions/50608941/typeerror-column-object-is-not-callable-when-use-case-when
import sys
from pyspark.sql.window import Window
from pyspark.sql import Row
import pyspark.sql.functions as func
from pyspark.sql import DataFrameStatFunctions as statFunc
from pyspark.sql.functions import coalesce, current_date, current_timestamp, lit, unix_timestamp, from_unixtime, \
    row_number, mean

a_df = sqlContext.table('opssup_dev_wrk_ct.wrk_ct_ods_batch_derived_extnd_stg2')
b_df = sqlContext.table('opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
fdsi_df = sqlContext.table('opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
ldsi_df = sqlContext.table('opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
fds_df = sqlContext.table('opssup_dev_wrk_ct.wrk_ct_sap_batch_specific_dates')
temp22_df = a_df \
    .join(b_df,(a_df.batch_number==b_df.Batch_Number)) \
    .join(fdsi_df,(a_df.First_DSI_BATCH_NUMBER==fdsi_df.Batch_Number),"left_outer") \
    .join(ldsi_df,(a_df.Last_DSI_BATCH_NUMBER==ldsi_df.Batch_Number),"left_outer") \
    .join(fds_df,(a_df.First_DS_BATCH_NUMBER==fds_df.Batch_Number),"left_outer") \
    .select( \
        a_df.driving_batch_number, \
        a_df.batch_number, \
        b_df.Material_Group, \
        a_df.mfg_stage_code, \
        func.when(a_df.batch_number==a_df.First_DSI_BATCH_NUMBER,lit('0')) \
            .otherwisw(lit('')) \
            .alias('mfg_start_date') \
           )