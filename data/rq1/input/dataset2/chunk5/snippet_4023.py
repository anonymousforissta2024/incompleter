#Source: https://stackoverflow.com/questions/51216128/gzip-python3-attributeerror-module-object-has-no-attribute-compress
pipe.setnx(prefix+item[0], gzip.compress(bytes(item[1], 'utf-8')))