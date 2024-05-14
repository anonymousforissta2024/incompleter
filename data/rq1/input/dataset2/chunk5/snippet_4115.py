#Source: https://stackoverflow.com/questions/44913006/nameerror-while-calling-module-declaring-default-values-in-a-class-function
from passlib.context import CryptContext
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Random import get_random_bytes