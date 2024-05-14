#Source: https://stackoverflow.com/questions/41285969/dropbox-api-v2-trying-to-upload-file-with-files-upload-throws-typeerror
with open("/home/pi/Desktop/dbox/asd.txt", "rb") as f:
    dbx.files_upload(f, '/asd.txt', mute = True)