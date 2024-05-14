#Source: https://stackoverflow.com/questions/76654972/filenotfound-error-in-python-3-even-though-i-see-the-file
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

list_stemmed_files = []
for i in filenames:
    with open (str(i),'r') as file:
        readFile = file.read()
        tokenized_file = nltk.tokenize.word_tokenize(readFile)
        stemmed_file = [ps.stem(word) for word in tokenized_file]
        list_stemmed_files.append(stemmed_file)