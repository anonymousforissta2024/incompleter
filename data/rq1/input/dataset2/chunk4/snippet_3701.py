#Source: https://stackoverflow.com/questions/61696944/error-in-having-a-sequence-typeerror-sequence-item-0-expected-str-instance
for i in range(len(tokenized)):
    tokenized[i] = ' '.join(tokenized[i])