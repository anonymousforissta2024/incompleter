#Source: https://stackoverflow.com/questions/53692117/attributeerror-list-object-has-no-attribute-isdigit-specifying-pos-of-each
import os, nltk, re
from nltk.corpus import stopwords
from unidecode import unidecode
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag


def read_data():
    global tokenized_raw_data
    with open("path//merge_text_results_pu.txt", 'r', encoding='utf-8', errors = 'replace') as f:
        raw_data = f.read()
        tokenized_raw_data = '\n'.join(nltk.line_tokenize(raw_data))
read_data()

def function1():
    tokens_sentences = sent_tokenize(tokenized_raw_data.lower())
    unfiltered_tokens = [[word for word in word_tokenize(word)] for word in tokens_sentences]
    tagged_tokens = nltk.pos_tag(unfiltered_tokens)
    nouns = [word.encode('utf-8') for word,pos in tagged_tokens
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos ==  'NNPS')]
    joined_nouns_text = (' '.join(map(bytes.decode, nouns))).strip()
    noun_tokens = [t for t in wordpunct_tokenize(joined_nouns_text)]
    stop_words = set(stopwords.words("english"))
function1()