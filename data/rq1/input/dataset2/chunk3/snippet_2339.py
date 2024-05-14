#Source: https://stackoverflow.com/questions/65324684/typeerror-lemmatize-missing-3-required-positional-arguments-index-except
df = pd.read_csv('file.csv', sep=';')

from nltk.corpus import stopwords

import re
from nltk.tokenize import RegexpTokenizer
from spacy.lang.fr import French


stop_words = set(stopwords.words('french'))
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
lemmatizer = French.Defaults.create_lemmatizer()


def clean_text(text):
    text = text.lower()  
    text = tokenizer.tokenize(text)
    text = [word for word in text if not word in stop_words]
    text = [lemmatizer.lemmatize(word) for word in text]
    final_text = ' '.join( [w for w in text if len(w)>2] ) 
    return final_text

df['comms_clean'] = df['comms'].apply(lambda x : clean_text(x))