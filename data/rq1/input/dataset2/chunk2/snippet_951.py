#Source: https://stackoverflow.com/questions/36378643/gmail-api-typeerror-sequence-item-0-expected-str-instance-bytes-found
credentials = get_credentials()
print(credentials)
print(str(credentials.invalid))
http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)