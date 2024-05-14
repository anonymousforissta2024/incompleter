#Source: https://stackoverflow.com/questions/55826705/pycryptodome-when-verifying-attributeerror-io-bufferedreader-object-has-no
def get_signature(message):
    h = SHA256.new(message)
    signature = pkcs1_15.new(priv_keyObj).sign(h)
    return signature

ENCODING = 'utf-8'

print(json.dumps({
    'EncryptedString':      base64.standard_b64encode(encrypted_data).decode(ENCODING),
    'SignedDataString':     base64.standard_b64encode(get_signature(encrypted_data)).decode(ENCODING),
}))