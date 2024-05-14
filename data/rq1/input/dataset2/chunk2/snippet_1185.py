#Source: https://stackoverflow.com/questions/58154711/python3-typeerror-a-bytes-like-object-is-required-not-str
r = requests.get('10.10.10.10/test_' + name, verify=True)