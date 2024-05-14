#Source: https://stackoverflow.com/questions/59516802/typeerror-a-bytes-like-object-is-required-not-str-xxxxxx
def create_key(x):
    import base64
    import os
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    password_provided = str(x)
    password = password_provided.encode()
    salt = b'\xfb|\xe8\xe0\xe5\x9d\x11\xf5\xbc 8o\xbe<\xd9\x92'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f1 = open('keys.key', 'ab')
    f1.write(key)
    f1.write(os.linesep)
    f1.close()


create_key('sairam')