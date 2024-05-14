#Source: https://stackoverflow.com/questions/56264449/typeerror-object-of-type-bytes-is-not-json-serializable
#!/usr/bin/python3

# Imports
import json
import base64
from cryptography.fernet import Fernet

# Save
def encrypt_string(string, f):
    return str(f.encrypt(base64.b64encode(bytes(string,'utf-8'))).decode('utf-8'))

def encrypt_dict(dict):
    fk = Fernet.generate_key().decode('utf-8')
    f = Fernet(fk)
    ed = {}
    ed['fk'] = base64.b64encode(bytes(fk, 'utf-8'))
    for key, value in dict.items():
        ekey = encrypt_string(key, f)
        evalue = encrypt_string(value, f)
        ed[ekey[::-1]] = evalue[::-1]
    return ed

def save_game(slot, savename):
    print("Saving file...")
    path = 'saves/savegame{0}.json'.format(slot)
    data = {
        'game': 'Game name here',
        'version': 'Version here',
        'author': 'Author here',
        'savename': str(savename),
    }
    data = encrypt_dict(data)
    with open(path, 'w') as f:
        json.dump(data, f)
        f.close()
    print('Data saved in', path)

# Main
import gamemodule as gm

def main():
    print("Running...")
    gm.save_game(1, 'test')
    input("Press any button to continue...")