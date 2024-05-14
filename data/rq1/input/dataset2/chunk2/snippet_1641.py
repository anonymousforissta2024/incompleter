#Source: https://stackoverflow.com/questions/68105958/typeerror-expected-str-bytes-or-os-pathlike-object-not-function
load_io_monthly_billing_to_snowflake = SnowflakeLoadOperator(
    task_id='load_io_monthly_billing_to_Snowflake',
    table=IOMonthlyBillingSnowflakeTable(),
    merge=False,
    partition=MonthlyBillingS3PartitionLatestFile(
        source_resolver=get_latest_io_monthly_billing_file_from_new_prefix,
        bucket=Variable.get('s3_bucket'),
        location_base="BTR/",
        partition_type=None
    )
)