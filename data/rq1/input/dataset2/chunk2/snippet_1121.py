#Source: https://stackoverflow.com/questions/48768084/nltk-unigramtagger-typeerror-unhashable-type-list
brown_tagged_sents = brown.tagged_sents()
brown_sents = brown.sents()

unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger.tag(brown_sents)
unigram_tagger.evaluate(brown_tagged_sents)