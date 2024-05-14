#Source: https://stackoverflow.com/questions/41285969/dropbox-api-v2-trying-to-upload-file-with-files-upload-throws-typeerror
import dropbox

dbx = dropbox.Dropbox("my_access_token")

data = "asd"

dbx.files_upload(data, '/file.txt')