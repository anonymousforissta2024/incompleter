#Source: https://stackoverflow.com/questions/65811328/why-do-i-get-a-typeerror-while-updating-hash-object
import string, random, hashlib 

def hash_and_salt(password):
    password_hash = hashlib.sha256()
    salt = ''.join(random.choice(string.digits) for i in range (8))
    password_hash.update(salt + password)
    return password_hash.hexdigest() , salt 



hash_and_salt(password="hello_world")