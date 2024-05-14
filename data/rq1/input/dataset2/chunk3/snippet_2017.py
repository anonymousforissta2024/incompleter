#Source: https://stackoverflow.com/questions/53697304/python-3-typeerror-utf-8-encode-must-be-str-not-bytes-using-requests
data = get_browser().result.get_page()
datafile = open(localfile, "w", encoding="utf-8")
datafile.write(data)
datafile.close()