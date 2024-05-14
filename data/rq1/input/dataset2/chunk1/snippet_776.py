#Source: https://stackoverflow.com/questions/33773157/word-tokenize-typeerror-expected-string-or-buffer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open('E:\\Book\\1500.txt', "r", encoding='ISO-8859-1') as File_1500:
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(File_1500)
    filtered_sentence = [w for w in words if not w in stop_words]
    print(filtered_sentence)