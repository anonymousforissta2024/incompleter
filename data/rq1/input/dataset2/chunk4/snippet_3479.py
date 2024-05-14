#Source: https://stackoverflow.com/questions/70981856/how-do-i-fix-the-typeerror-load-missing-1-required-positional-argument-load
from openai.embeddings_utils import get_embedding

# This will take just under 10 minutes
df['babbage_similarity'] = df.combined.apply(lambda x: get_embedding(x, engine='text-similarity-babbage-001'))
df['babbage_search'] = df.combined.apply(lambda x: get_embedding(x, engine='text-search-babbage-doc-001'))
df.to_csv('/content/documents.csv')