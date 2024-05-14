#Source: https://stackoverflow.com/questions/59481105/typeerror-an-asyncio-future-a-coroutine-or-an-awaitable-is-required
import bs4
import asyncio
import aiohttp


async def parse(page):
    soup=bs4.BeautifulSoup(page,'html.parser')
    soup.prettify()
    print(soup.title)



async def request():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://google.com") as resp:
            await parse(resp)



loop=asyncio.get_event_loop()
loop.run_until_complete(request)