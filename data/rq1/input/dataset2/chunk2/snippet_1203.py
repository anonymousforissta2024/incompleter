#Source: https://stackoverflow.com/questions/53005229/typeerror-a-bytes-like-object-is-required-not-str-in-run-line-line-split
with open(fname, 'rb') as f:
    lines = [x.strip() for x in f.readlines()]

for line in lines:
    tmp = line.strip().lower()
    if 'some-pattern' in tmp: continue
    # ... code