#Source: https://stackoverflow.com/questions/64113949/attributeerror-bytes-object-has-no-attribute-encode-in-python-3-6
import requests
import json
import pymssql
from pymongo import MongoClient
from datetime import datetime
from cryptography.fernet import Fernet

encrypted_pwd='gAAAAABfcsCIlNNosZ2bWzUDueAVoIPjUFOqjNCOIOTUrOkrf_TK2FaC1L5b0VXo2ZKBz1VYA25jVfXBQQ5Y-vwTZA7339onZw=='

def vantiveDvDBConnection():
    conn = pymssql.connect('abc.def.ad.is.net:5010','itcompl',decrypt_message(encrypted_pwd), 'VN2DV')
    return conn

def decrypt_message(enc_message):
    print("inside decrypt")
    key=load_key()
    print(key)
    f=Fernet(key)
    print(enc_message.encode())
    decrypt_message=f.decrypt(enc_message.encode())
    return decrypt_message
                                                                           