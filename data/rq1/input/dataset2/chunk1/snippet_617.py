#Source: https://stackoverflow.com/questions/44862228/proxybroker-attributeerror-dict-object-has-no-attribute-expired
import asyncio
from proxybroker import Broker

async def use(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        elif 'SOCKS5' in proxy.types:  # filter by type
            print('Found SOCKS5 proxy: %s' % proxy)
        else:
            print('Found proxy: %s' % proxy)

async def find(proxies, loop):
    broker = Broker(queue=proxies,
                    timeout=8,
                    attempts_conn=3,
                    max_concurrent_conn=200,
                    judges=['https://httpheader.net/', 'http://httpheader.net/'],
                    providers=['http://www.proxylists.net/', 'http://fineproxy.org/eng/'],
                    verify_ssl=False,
                    loop=loop)

    # only anonymous & high levels of anonymity for http protocol and high for others:
    types = [('HTTP', ('Anonymous', 'High')), 'HTTPS', 'SOCKS4', 'SOCKS5']
    countries = ['US', 'GB', 'DE']
    limit = 10

    await broker.find(types=types, countries=countries, limit=limit)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    proxies = asyncio.Queue(loop=loop)
    tasks = asyncio.gather(find(proxies, loop), use(proxies))
    loop.run_until_complete(tasks)