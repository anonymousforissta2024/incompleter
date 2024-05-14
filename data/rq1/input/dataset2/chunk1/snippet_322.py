#Source: https://stackoverflow.com/questions/60156335/cloud-function-attribute-error-bytes-object-has-no-attribute-get-when-readi
storage_client = storage.Client()
bucket_name = 'bucket_name'
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.get_blob('key.json')
json_data_string = blob.download_as_string()

credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    json_data_string,
    scopes=['https://www.googleapis.com/auth/analytics',
            'https://www.googleapis.com/auth/analytics.edit'])