#Source: https://stackoverflow.com/questions/72095459/typeerror-token-must-be-bytes-when-it-is-already-bytes
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def decrypt_data(key, data):
    key = bytes(key.encode('utf-8'))
    SALT = b'\xbf\xd4\xa9\xcei\xfa\xa7Db\x83\xbf\xa5.\xbe/\xd9'

    kdf = PBKDF2HMAC(
        hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=32000
    )
    fernet = Fernet(base64.urlsafe_b64encode(kdf.derive(key)))
    return fernet.decrypt(data)

def encrypt_data(key, data):
    key = bytes(key.encode('utf-8'))
    SALT = b'\xbf\xd4\xa9\xcei\xfa\xa7Db\x83\xbf\xa5.\xbe/\xd9'

    kdf = PBKDF2HMAC(
        hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=32000
    )

    key = base64.urlsafe_b64encode(kdf.derive(key))
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())