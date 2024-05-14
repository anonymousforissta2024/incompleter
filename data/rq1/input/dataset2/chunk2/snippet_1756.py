#Source: https://stackoverflow.com/questions/71565180/typeerror-a-bytes-like-object-is-required-not-binary-when-using-boto3-and-dy
async def authenticate(email: str = Form(...), password: str = Form(...)):
    response = table.get_item(Key={'email': email})
    item = response['Item']
    stored_salt = item['salt']
    stored_password = item['password']
    ...