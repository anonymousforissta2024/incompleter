#Source: https://stackoverflow.com/questions/41384654/python3-pymongo-typeerror-nonetype-object-is-not-subscriptable-within-cla
import pymongo
class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['cvm']

    @staticmethod
    def find_sort(collection, query, direction, limit):
        return Database.DATABASE[collection].find({}).sort(query, direction).limit(limit)