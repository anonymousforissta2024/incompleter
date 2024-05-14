#Source: https://stackoverflow.com/questions/58777341/typeerror-str-object-is-not-callable-for-uuid-value-python-3
import uuid

hash_val = uuid.uuid4().hex()

print(hash_val)