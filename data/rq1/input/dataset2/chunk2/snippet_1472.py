#Source: https://stackoverflow.com/questions/67142181/attributeerror-bytes-object-has-no-attribute-hexdigest
import requests
import hashlib 

def request_api_data (query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)
    if res.status_code != 200:
        print('it is an error')
        #raise RuntimeError(f'Error fetching: {res.status_code}, check api and try again')
        return res
request_api_data('123')

def pwned_api_check(password):
    sha1password= hashlib.sha1(password.encode('utf-8').hexdigest().upper())
    
    print (sha1password)

    #return sha1password

pwned_api_check('123')  