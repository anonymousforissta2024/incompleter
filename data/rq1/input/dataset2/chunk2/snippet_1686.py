#Source: https://stackoverflow.com/questions/55826705/pycryptodome-when-verifying-attributeerror-io-bufferedreader-object-has-no
def verify_signature(message, signature):
    h = SHA256.new(message)
    try:
        pkcs1_15.new(pub_key_new).verify(h, signature)
        print("The signature is valid.")
    except (ValueError, TypeError):
        print("The signature is not valid.")

verify_signature(base64.standard_b64decode(data['EncryptedString']), base64.standard_b64decode(data['SignedDataString']))