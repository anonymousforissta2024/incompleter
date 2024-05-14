#Source: https://stackoverflow.com/questions/47863796/type-error-encountered-while-working-on-custom-encode-in-python-3-6
import os
import sys
import base64

def encode(key, clear):
    """encode custom """
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        #change the int or str
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))

clear = "ABCDEFGH"
encode_var = encode("crumbs", clear)