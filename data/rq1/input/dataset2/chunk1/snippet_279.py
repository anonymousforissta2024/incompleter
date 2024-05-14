#Source: https://stackoverflow.com/questions/51804916/struct-unpack-type-error-a-byte-like-object-is-required-not-str-unpack-a
list1 = [b'\x03\x00\x00\x00\xff\xff\xff\xff',
b'\x07\x00\x00\x00\x06\x00\x00\x00\xff\xff\xff\xff']

print(struct.unpack('<s', bytes(i)))