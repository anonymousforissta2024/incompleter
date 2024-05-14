#Source: https://stackoverflow.com/questions/77079339/getting-attributeerror-when-using-pickle-on-a-python-function
udf_bytes = s3_client.get_object(Bucket="Bucket_name", Key="key")["Body"].read()

downloaded_func = pickle.loads(udf_bytes)