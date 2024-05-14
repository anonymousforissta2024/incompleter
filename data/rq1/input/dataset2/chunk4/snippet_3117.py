#Source: https://stackoverflow.com/questions/65006689/gensim-taggeddocument-list-generates-typeerror-nonetype-object-is-not-iterabl
class doc2vec_model(Doc2Vec):
    
    def train(self,path):
        self._path = path
        self._tagged_documents()

        super(Doc2Vec, self).__init__(self._docs, min_count = 100, 
                                     vector_size=300, 
                                     epochs = 20, 
                                     negative = 5, 
                                     workers=20, 
                                     sample = 1e-5,
                                     alpha=0.01,
                                     min_alpha=0.0001)

    def _tagged_documents(self,):
        self.file_l = [name for name in glob.iglob(self._path, recursive=True)]
        self._docs = [] 
        for f_id, path in enumerate(self.file_l):
            with open(path,'r') as f:
                docu = f.read()
                docu = norm_string(docu)
                docu = docu.split(' ')
                chunk_size = 200 
                chunk_l = [docu[i:i+chunk_size] for i in range(0,len(docu),chunk_size)]
                for c_id, docu_chunk in enumerate(chunk_l):
                    self._docs.append(TaggedDocument(words=docu_chunk, tags=(f'DOC_{f_id}_{c_id}',)))