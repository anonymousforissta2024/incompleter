#Source: https://stackoverflow.com/questions/76131938/typeerror-can-only-concatenate-list-not-str-to-list-when-upload-to-aws-s3-b
AccountName = ["AWSAccountName"]

def upload_s3(AccountName,bucket,filename):
    dir = os.getcwd()
    s3 = boto3.client('s3')
    #prefix = 'folder_' + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "/" + filename
    prefix =  AccountName + 'folder_' + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "/" + filename
    #s3object = s3.put_object(Bucket=bucket, Key=prefix)
    s3.upload_file(dir + '/' +filename, bucket, prefix)

if __name__ == "__main__":
    upload_s3(AccountName, "ec2-idle-workspace-list","EC2_Idle_info_cpu_NetworkIn_NetworkOut.csv")