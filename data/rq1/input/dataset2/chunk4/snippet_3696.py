#Source: https://stackoverflow.com/questions/50665581/attributeerror-textchunker-object-has-no-attribute-print-chunks
import numpy as np
from nltk.corpus import brown

# Split the input text into chunks, where
# each chunk contains N words
class textChunker:

    def __init__(self, input_data='', chunk_size=0):

        self.input_data = input_data
        self.chunk_size = chunk_size

    def chunker(self,input_data, N):
        input_words = input_data.split(' ')
        output = []

        cur_chunk = []
        count = 0
        for word in input_words:
            cur_chunk.append(word)
            count += 1
            if count == N:
                output.append(' '.join(cur_chunk))
                count, cur_chunk = 0, []

        output.append(' '.join(cur_chunk))

        return output

        def print_chunks(self,input_data,chunk_size):
            import chunker
            chunks = chunker(input_data, chunk_size)
            print('\nNumber of text chunks =', len(chunks), '\n')
            for i, chunk in enumerate(chunks):
                print('Chunk', i + 1, '==>', chunk[:50])

if __name__=='__main__':

    input_data = ' '.join(brown.words()[:12000])
    chunk_size = 700

    text_Chunker=textChunker()
    printchunks =text_Chunker.print_chunks(input_data,chunk_size)