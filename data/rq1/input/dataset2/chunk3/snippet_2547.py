#Source: https://stackoverflow.com/questions/35919525/type-error-in-python-3-expected-string-or-buffer-but-u-occured-at-index-0
token_pattern=r'(?u)\b\w\w+\b'
def preprocess(line,
           token_pattern=token_pattern,
           exclude_stoptword=config.cooccurrence_word_exclude_stopword,
           encode_digit=False):

    token_pattern=re.compile(token_pattern,re.UNICODE)
    tokens=[x.lower() for x in token_pattern.findall(line)]

    tokens_stemmed=stem_tokens(tokens,english_stemmer)
    if exclude_stoptword:
        tokens_stemmed=[x for x in tokens_stemmed if x  not in stopwords]
    return tokens_stemmed

def extract(df):
    #Unigram Features 

    df["query_unigram"]=list(df.apply(lambda x:preprocess(df["query"]),axis=1))