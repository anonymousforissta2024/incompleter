#Source: https://stackoverflow.com/questions/52233295/typeerrora-bytes-like-object-is-required-not-str-when-reading-from-a-file
authors_file_handler = open(authors_file, "r")
authors = pickle.load(authors_file_handler)
authors_file_handler.close()