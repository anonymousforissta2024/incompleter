#Source: https://stackoverflow.com/questions/74637643/typeerror-argument-of-type-int-is-not-iterable-in-aes-algorithm-using-python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = 'QwroeApp90652321'
AES.key_size=128
AES.block_size=128
plaintext = "wdrdooloo"
cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
msg =cipher.encrypt(pad(plaintext.encode('utf8'), 16))
print(msg.hex())