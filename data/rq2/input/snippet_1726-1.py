import json
from collections import namedtuple
x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print(x.name, x.id, x.location)