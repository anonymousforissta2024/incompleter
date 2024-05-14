#Source: https://stackoverflow.com/questions/55775131/nltk-package-returns-typeerror-lazycorpusloader-object-is-not-callable
import nltk.corpus as stopwords
import nltk
nltk.download("stopwords")
sw = stopwords.words('english')