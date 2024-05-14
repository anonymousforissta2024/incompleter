#Source: https://stackoverflow.com/questions/27995090/typeerror-raised-by-bytes-join-when-passing-in-a-byte-object
header = struct.pack(STRFMT, MAGIC, VERSION,
            command, self.seq, self.session)

data = dataStr.encode() # dataStr is a String

print(type(header)) # <class 'bytes'>
print(type(header)) # <class 'bytes'>

header.join(data)