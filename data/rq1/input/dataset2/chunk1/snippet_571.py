#Source: https://stackoverflow.com/questions/32071536/typeerror-sequence-item-0-expected-str-instance-bytes-found
for line in fo:
    line = " ".join(line.split())
    line = line.strip()