#Source: https://stackoverflow.com/questions/61973622/attributeerror-dict-object-has-no-attribute-split
columns = []
rows = []
chunks = body.split('}')
for chunk in chunks:
    row = []
    if len(chunk)>1:
        entry = chunk.replace('{','').strip().split(',')
        for e in entry:
            item = e.strip().split(':')
            if len(item)==2:
                row.append(item[1])
                if chunks.index(chunk)==0:
                    columns.append(item[0])
        rows.append(row)
df = pd.DataFrame(rows, columns = columns)
df.head()

df.to_csv ('r3edata.csv', index = False, header = True)