#Source: https://stackoverflow.com/questions/59028666/attributeerror-module-queue-has-no-attribute-simplequeue
async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    resp = await session.request(method='GET', url=url, **kwargs)
    resp.raise_for_status()
    html = await resp.text()
    return html

async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
    urls = [
        'https://regex101.com/'
    ]
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_html(url=url, session=session, **kwargs))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(bulk_crawl_and_write(file=None, urls=None))