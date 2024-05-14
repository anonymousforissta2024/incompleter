#Source: https://stackoverflow.com/questions/59577129/python3-concatenate-str-not-bytes-to-bytes-typeerror
with open(os.path.abspath(file_path) + ".cap" , 'wb') as f: f.write(data)