#Source: https://stackoverflow.com/questions/77350345/asyncio-gather-typeerror-an-asyncio-future-a-coroutine-or-an-awaitable-is
import asyncio
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession

async def fetch_proxies(url):
    session = AsyncHTMLSession()
    webpage = await session.get(url) # headers=headers
    await session.close()
    soup = BeautifulSoup(webpage.html.raw_html, 'lxml')
    tag = soup.find('textarea', {'class':'form-control'})
    return tag.text

async def check_valid_proxy(proxy):
    try:
        session = AsyncHTMLSession()
        webpage = await session.get('https://ifconfig.me', proxies = {'https' : proxy})
        await session.close()
        return proxy
    except Exception as err:
        print(err)

async def main():
    url = 'https://free-proxy-list.net'
    proxy_fetch = await fetch_proxies(url)
    proxy_list = proxy_fetch.split('\n')[3:-1]
    tasks = []
    for proxy in proxy_list:
        task = asyncio.create_task(check_valid_proxy(proxy))
        tasks.append(task)
        tasks.append(await asyncio.sleep(.1))
    valid_proxies = asyncio.gather(*tasks)
    return valid_proxies

loop = asyncio.get_event_loop()
valid_proxy_list = loop.run_until_complete(main())
print(valid_proxy_list)