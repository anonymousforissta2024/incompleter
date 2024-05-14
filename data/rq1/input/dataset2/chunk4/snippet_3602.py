#Source: https://stackoverflow.com/questions/44243530/typeerror-when-creating-a-sha512-hash-using-pycryto
signature = f[:signatureLength]
f = open('lib/publicKey.pem','rb')
publicKey = RSA.importKey(f.read())
hash = SHA512.new(f[signatureLength:])
verification = PKCS1_PSS.new(publicKey)