#Source: https://stackoverflow.com/questions/75822550/typeerror-cannot-pickle-thread-lock-object
def __init__(self, client: pymongo.MongoClient) -> None:
    self.client = client
    self.api = AmazonApiManager()