#Source: https://stackoverflow.com/questions/68148898/attributeerror-int-object-has-no-attribute-split-for-pandas
df['doc_len'] = df['Content'].apply(lambda words: len(words.split()))