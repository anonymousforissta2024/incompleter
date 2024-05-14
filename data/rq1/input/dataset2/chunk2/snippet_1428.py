#Source: https://stackoverflow.com/questions/43023315/python3-typeerror-a-bytes-like-object-is-required-not-str
content = b''.join(str(line) for line in vecfile.readlines())