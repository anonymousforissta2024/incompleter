import collections
import pprint
with open(file_input, 'r') as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)
print(value)