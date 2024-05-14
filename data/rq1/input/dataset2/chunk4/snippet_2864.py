#Source: https://stackoverflow.com/questions/74904901/python-google-voice-api-login-error-attributeerror-nonetype-object-has-no-at
from googlevoice import Voice
import keyring

if __name__ == '__main__':
    gv = Voice()
    usr = keyring.get_password('2', '2')
    pwd = keyring.get_password('1', '1')
    client = gv.login(usr,pwd)