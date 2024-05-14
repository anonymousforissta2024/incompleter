#Source: https://stackoverflow.com/questions/27519306/hashlib-md5-typeerror-unicode-objects-must-be-encoded-before-hashing
import hashlib
a = hashlib.md5()
a.update('hi')
a.digest()