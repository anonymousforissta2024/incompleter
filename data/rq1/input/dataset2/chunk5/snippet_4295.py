#Source: https://stackoverflow.com/questions/60084673/typeerror-unhashable-type-list-when-using-nltk-freqdist-on-pandas-series
#divide to words
tokenizer = RegexpTokenizer(r'\w+')
df['tokenized_sents'] = df['Responses'].apply(nltk.word_tokenize)