#Source: https://stackoverflow.com/questions/59577129/python3-concatenate-str-not-bytes-to-bytes-typeerror
file_path = "subfolder\a_file.bin"

with file(file_path + ".cap", "wb") as f: f.write(data)