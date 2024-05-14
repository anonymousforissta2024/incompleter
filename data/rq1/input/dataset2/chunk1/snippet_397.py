#Source: https://stackoverflow.com/questions/69994834/attributeerror-aioclientcreator-object-has-no-attribute-register-lazy-block
session = sagemaker.Session()
region = boto3.Session().region_name
role = get_execution_role()

import pyarrow.parquet as pq
import s3fs
s3 = s3fs.S3FileSystem()

bucket = 's3://xx'

df = pq.ParquetDataset(bucket, filesystem=s3).read_pandas().to_pandas()