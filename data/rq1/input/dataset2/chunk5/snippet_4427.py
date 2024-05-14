#Source: https://stackoverflow.com/questions/65705471/concatenating-dataframes-read-from-multiple-aws-s3-bucket-generate-nonetype-erro
bucket = s3.Bucket('mybucket')
import io
prefix_objs = bucket.objects.filter(Prefix="folder/file_prefix")

df = pd.DataFrame()

for obj in prefix_objs:
    key = obj.key
    body = obj.get()['Body'].read()
    temp = pd.read_csv(io.BytesIO(body), sep=",",encoding='utf8')        
    frame =[df,temp]
    df = pd.concat(frame)