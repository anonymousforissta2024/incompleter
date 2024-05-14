#Source: https://stackoverflow.com/questions/35249879/python-struct-unpack-errors-with-typeerror-a-bytes-like-object-is-required-not
value = struct.unpack("<h",chr(b)+chr(a))[0]