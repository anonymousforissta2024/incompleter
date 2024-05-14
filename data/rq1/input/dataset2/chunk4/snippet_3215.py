#Source: https://stackoverflow.com/questions/77313190/filtering-pymongo-list-collection-names-throws-type-error
myclient = pymongo.MongoClient('x.x.x.x', username='xxxxxx', 
            password='yyyyyyy', authSource='zzzz', authMechanism='SCRAM-SHA-256')
mydb = myclient["db"]    
filter = {"name": {"$regex": r"^(?!system\.)"}}
collection = mydb.list_collection_names(filter=filter)
collection.sort()
filtered_names = list(filter(lambda x: "test" in x, collection ))