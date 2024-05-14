#Source: https://stackoverflow.com/questions/70657867/nameerror-name-encode-is-not-defined-while-trying-to-format-an-object-to-j
import json

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


bob = person("Bob", 5)


class encode_Obj:

    def encode(x):
        if isinstance(x, person):
            return {"name": x.name, "age": x.age}
        else:
            raise TypeError("Object of type user is not JSON serializable")


bob_JSON = json.dumps(bob, default=encode)
print(bob_JSON)