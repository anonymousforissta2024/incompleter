#Source: https://stackoverflow.com/questions/48040985/hexdigest-throws-typeerror-required-argument-length-pos-1-not-found
import hashlib


arguments = [[hashlib.md5('hello'.encode())]]
f = open('Dictionary.txt', 'r')
words = f.readlines()
f.close()
# Remember to strip the \n's
cracked = {}
for ciphertext in arguments[0]:
    for word in words:
        for alg in hashlib.algorithms_guaranteed:
            exec("hashed = hashlib.{}(word.encode())".format(alg))
            if hashed.hexdigest() == ciphertext:
                cracked[ciphertext] = [word, alg]
                print("[+] Found {} as {} with {} algorithm!".format(ciphertext, word, alg))
                break
print(cracked)