#Source: https://stackoverflow.com/questions/62903409/typeerror-string-argument-expected-got-bytes
data = "2a2b2c2a2b2c2a2b2c2a2b2cb1"
buf = io.StringIO()    
for line in data.splitlines():
    line = line.strip().replace(" ", "")
    if not line:
        continue
    bytez = binascii.unhexlify(line)
    buf.write(bytez)

with open("image.jpg", "wb") as f:
    f.write(buf.getvalue()) 