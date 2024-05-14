#Source: https://stackoverflow.com/questions/66972367/getting-typeerror-method-takes-0-positional-arguments-but-1-was-given-with-s
import corpus as corp

def main():
    corpus = corp.Corpus("review.txt")
    corpus_list = corpus.corpus_to_list()
    print(corpus_list)

if __name__ == "__main__":
    main()