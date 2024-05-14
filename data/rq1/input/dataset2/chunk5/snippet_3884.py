#Source: https://stackoverflow.com/questions/32045794/s3fs-typeerror-cant-concat-bytes-to-str
import fs.s3fs
myfs = fs.s3fs.S3FS(bucket, prefix, aws_access_ke, aws_secret_key)
myfs.listdir()