#Source: https://stackoverflow.com/questions/60975722/attributeerror-bytes-object-has-no-attribute-encode-in-python-3
if _charset is None:
        try:
            _text.encode('us-ascii')
            _charset = 'us-ascii'
        except UnicodeEncodeError:
            _charset = 'utf-8'