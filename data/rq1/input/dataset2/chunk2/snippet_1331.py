#Source: https://stackoverflow.com/questions/47267198/attributeerror-bool-object-has-no-attribute-read-when-calling-requests-post
upload_headers = {'Authorization':'Bearer' + ' ' + access_token, 'X-Backtory-Storage-Id':'48378438**********'}
upload_data = {'fileItems[0].fileToUpload': open('file.txt', 'rb'), 'fileItems[0].path': r'/path1/', 'fileItems[0].replacing': True}
upload_response = requests.post("http://storage.backtory.com/files", files=upload_data, headers=upload_headers)
print(upload_r)