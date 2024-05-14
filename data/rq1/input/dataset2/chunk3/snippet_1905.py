#Source: https://stackoverflow.com/questions/70096375/fasttext-typeerror-loadmodel-incompatible-function-arguments
import fasttext
from pathlib import Path

base_path = Path("..")
fasttext_model = base_path / "models" / "cc.de.300.bin"

class EmbeddingVectorizer:
    def __init__(self):

        self.embedding_model = fasttext.load_model(fasttext_model)

    def __call__(self, doc):
        """
        Convert address to embedding vectors
        :param address: The address to convert
        :return: The embeddings vectors
        """
        embeddings = []
        for word in doc:
            embeddings.append(self.embedding_model[word])
        return embeddings

embedding_model = EmbeddingVectorizer()