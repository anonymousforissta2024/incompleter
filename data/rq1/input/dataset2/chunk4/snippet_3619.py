#Source: https://stackoverflow.com/questions/47732146/python-3-inheritance-attributeerror-how-to-solve-it
class AttackDB(MongoData):
    __metaclass__  = abc.ABCMeta

    def __init__(self, db_name, coll_name):
        MongoData.__init__(self, db_name, coll_name)

    @abc.abstractmethod
    def writeDB(self, wdict):
        doc_id = self.__coll.insert_one(attack).inserted_id
        print("Attack with id {} was inserted in the DB.".format(dic_id))