#Source: https://stackoverflow.com/questions/43849689/py-corenlp-typeerror-string-indices-must-be-integers
from pycorenlp import StanfordCoreNLP
from newspaper import Article

url = u'newsArticle.example.html'
nlp = StanfordCoreNLP('http://localhost:9000')
article = Article(url)
article.download()
article.parse()


LARGE_TEXT=article.text


res = nlp.annotate(LARGE_TEXT,
               properties={
                   'annotators': 'sentiment',
                   'outputFormat': 'json',
                   'timeout': 1000,
               })
for s in res["sentences"]:
    print ("%d: '%s': %s %s" % (
        s["index"],
        " ".join([t["word"] for t in s["tokens"]]),
        s["sentimentValue"], s["sentiment"]))