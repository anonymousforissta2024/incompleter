#Source: https://stackoverflow.com/questions/42098053/typeerror-object-takes-no-parameters-in-python-3-x
class Media:
    _id = None
    _taken_time = None

    def __init__(self, id=None, taken_time=None):
        self._id = id
        self._taken_time = taken_time

    @property
    def id(self):
        return self._id

    @yguid.setter
    def id(self, value):
        self._id = value

    @property
    def taken_time(self):
        return self._taken_time

    @taken_time.setter
    def taken_time(self, value):
        self._taken_time = value

    def serialize(self):
        return {
            "id": self._id,
            "taken_time": self._taken_time
        }