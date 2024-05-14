#Source: https://stackoverflow.com/questions/76626739/python-typeerror-cant-instantiate-abstract-class-with-abstract-methods
class ChromaProductRetriever(BaseRetriever, BaseModel):
    vectorstore: VectorStore
 
    class Config:
        arbitrary_types_allowed = True
 
    def combine_metadata(self, doc) -> str:
        metadata = doc.metadata
        return (
           "Item Name: " + metadata["item_name"] + ". " +
           "Item Description: " + metadata["bullet_point"] + ". " +
           "Item Keywords: " + metadata["item_keywords"] + "."
        )
 
    def get_relevant_documents(self, query):
        docs = []
        for doc in self.vectorstore.similarity_search(query):
            content = self.combine_metadata(doc)
            docs.append(Document(
                page_content=content,
                metadata=doc.metadata
            ))
 
        return docs