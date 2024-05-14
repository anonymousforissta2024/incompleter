#Source: https://stackoverflow.com/questions/58161798/attributeerror-float-object-has-no-attribute-split-while-running-larger-dat
def build_vocab(sentences, verbose=True):

    vocab = {}

    for sentence in tqdm(sentences):
        for word in sentence:
            try:
                vocab[word] += 1
            except KeyError:
                vocab[word] = 1

    return vocab    
sentences = train_df["question_text"].progress_apply(lambda x: x.split()).values
vocab = build_vocab(sentences)