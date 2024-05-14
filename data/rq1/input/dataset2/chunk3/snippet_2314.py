#Source: https://stackoverflow.com/questions/48040985/hexdigest-throws-typeerror-required-argument-length-pos-1-not-found
import hashlib
import random


def dict_attack(pwds):
    f = open('Dictionary.txt', 'r')
    words = f.readlines()
    f.close()
    cracked = []
    for pwd in pwds:
        for w in words:
            word = w.strip('\n')
            word = word.strip(' ')
            hashed = hashlib.md5(word.encode())
            if hashed.hexdigest() == pwd:
                print("[+] Found {} as {}, updating...".format(pwd, word))
                cracked.append(word)
                break
    print("[-] {}/{} passwords found!".format(len(cracked), len(pwds)))
    return cracked

def main():
    # To generate new ciphertext
    f = open('Dictionary.txt', 'r')
    words = f.readlines()
    f.close()
    for b in range(0, 10):
        passwords.append(random.choice(words))
        passwords[b] = passwords[b].strip('\n')
        passwords[b] = passwords[b].strip(' ')
    hashed_passwords = []
    for p in passwords:
        hashed_passwords.append(hashlib.md5(p.encode()).hexdigest())
    #print(hashed_passwords)
    print(dict_attack(hashed_passwords))

main()