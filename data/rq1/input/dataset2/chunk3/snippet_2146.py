#Source: https://stackoverflow.com/questions/68118319/typeerror-object-type-class-str-cannot-be-passed-to-c-code-using-pycryptodo
from base64 import b64encode, b64decode
from Crypto.Cipher import AES

SOME_SECRET_KEY = 'HPo7OLqB4Fkk4E2yGOtwqw8H5fHR9kNx67OR4g4UdlA='
SOME_IV = 'p5ldmBPdd/9pjC0bDC/nSg=='
secret_key_in_bytes = bytes(b64decode(SOME_SECRET_KEY))
iv_in_bytes = bytes(b64decode(SOME_IV))

def decrypt_with_padding(data):
    cypto_obj = AES.new(secret_key_in_bytes, AES.MODE_CBC, iv_in_bytes)
    decrypted = cypto_obj.decrypt(b64decode(data))
    bytes_to_string = decrypted.decode("utf-8")
    decrypted_data = pkcs5_unpad(bytes_to_string)
    return decrypted_data


def encrypt_with_padding(data):
    cypto_obj = AES.new(secret_key_in_bytes, AES.MODE_CBC, iv_in_bytes)
    encrypted_data = cypto_obj.encrypt(pkcs5_pad(str(data)))
    return b64encode(encrypted_data).decode()


def pkcs5_pad(s, BLOCK_SIZE=16):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(
        BLOCK_SIZE - len(s) % BLOCK_SIZE
    )


def pkcs5_unpad(s):
    return s[0: -ord(s[-1])]


if __name__ == "__main__":
    data = '{"idServicio":79, "idProducto":209 , "referencia": "40425475190118187271", "montoPago": 9999, "telefono":"1111111111", "horaLocal":"20200401222821"}'
    encrypted = encrypt_with_padding(data)
    print(encrypted)
    decrypted = decrypt_with_padding(encrypted)
    print(decrypted)