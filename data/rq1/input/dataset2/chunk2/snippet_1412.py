#Source: https://stackoverflow.com/questions/72095459/typeerror-token-must-be-bytes-when-it-is-already-bytes
from cryptography.fernet import InvalidToken
from framework.local_storage_encryption import encrypt_data, decrypt_data

# get_history() ->
# -1: unknown exception
# 0: success
# 1: invalid key

def get_history(key):
    try:
        value = []
        string_plain = decrypt_data(key, open('local_storage/HISTORY').readlines())
        for url in string_plain.split("\n"):
            value.append(url)
        return value
    except InvalidToken as exc:
        print(f"[!!!] Unable to load search history as the decryption key provided is invalid.")
        return [], 1

    return [], -1

def save_history(key, value: list):
    string_plain = ""
    for url in value:
        string_plain += f"{url}\n"

    with open('local_storage/HISTORY', 'wb') as file:
        file.write(encrypt_data(key, string_plain))

history = get_history("test") # this function itself raises the error