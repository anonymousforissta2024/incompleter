#Source: https://stackoverflow.com/questions/68793171/python-typeerror-asyncio-future-object-is-not-subscriptable
import asyncio
import requests

jsonHashes = {}
responses = []

def pinToIPFS(number):
    url = 'https://api.pinata.cloud/pinning/pinFileToIPFS'
    par = {
        'pinata_api_key': 'blabla',
        'pinata_secret_api_key': 'blabla'
    }
    file = {'file': open(str(number) + '.jpg', 'rb')}

    res = requests.post(url, headers = par, files = file)
    jsonHashes[res.json()['IpfsHash']] = number
    print(res.json()['IpfsHash'] + ' = ' + str(number))


async def main():
    loop = asyncio.get_event_loop()
    futures = []
    for i in range(2):
        futures = loop.run_in_executor(None, pinToIPFS, i)
    for i in range(2):
        jsonHashes[await futures[i].json()['IpfsHash']] = i
    

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


print(jsonHashes)