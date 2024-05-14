#Source: https://stackoverflow.com/questions/61695553/typeerror-unicode-objects-must-be-encoded-before-hashing-python2-working-but-py
hashlib.sha256(re.sub('[^a-zA-Z0-9]', "", each_user["Merchandiser"]).lower()[
                                           :4].capitalize() + "@123").hexdigest()