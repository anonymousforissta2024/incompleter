#Source: https://stackoverflow.com/questions/53847237/audiosegment-and-bytesio-module-gives-filenotfounderror
import boto3
from pydub import AudioSegment
import io
client = boto3.client('s3')
obj = client.get_object(Bucket='<BucketName>', Key='<FileName>')
data = io.BytesIO(obj['Body'].read())
sound1 = AudioSegment.from_file(data)