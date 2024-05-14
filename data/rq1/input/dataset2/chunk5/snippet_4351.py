#Source: https://stackoverflow.com/questions/65705471/concatenating-dataframes-read-from-multiple-aws-s3-bucket-generate-nonetype-erro
bucket = s3.Bucket('my bucket')
import io
prefix_objs = bucket.objects.filter(Prefix="folder/prefix")

df = []

for obj in prefix_objs:
    key = obj.key
    body = obj.get()['Body'].read()
    temp = pd.read_csv(io.BytesIO(body), encoding='utf8',sep=",")        
    df.append(temp)