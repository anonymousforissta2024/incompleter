#Source: https://stackoverflow.com/questions/49465554/try-to-build-webserver-and-read-html-file-with-typeerror-must-be-str-not-byte
file = open('index.html', 'r')
index_content += file.read()
file.close()