#Source: https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-handling-file-conte
with open(fname, 'rb') as f:
    lines = [x.strip() for x in f.readlines()]

for line in lines:
    tmp = line.strip().lower()
    if 'some-pattern' in tmp: continue
    # ... code