#Source: https://stackoverflow.com/questions/32045794/s3fs-typeerror-cant-concat-bytes-to-str
prefix += chr(i%256).encode('utf-8') 