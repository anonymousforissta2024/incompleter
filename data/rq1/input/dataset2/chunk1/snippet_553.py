#Source: https://stackoverflow.com/questions/48625933/python-async-attributeerror-aexit
import aiohttp
import asyncio
import tqdm


async def fetch_url(session_, url_, timeout_=10):
    with aiohttp.Timeout(timeout_):
        async with session_.get(url_) as response:
            text = await response.text()
            print("URL: {} - TEXT: {}".format(url_, len(text)))
            return text


async def parse_url(session, url, timeout=10):
    # get doc from url
    async with await fetch_url(session, url, timeout) as doc:
        print("DOC: {}".format(doc, len(doc)))
        return doc


async def parse_urls(session, urls, loop):
    tasks = [parse_url(session, url) for url in urls]
    responses = [await f for f in tqdm.tqdm(asyncio.as_completed(tasks), total = len(tasks))]
    return responses


if __name__ == '__main__':

    tickers = ['CTXS', 'MSFT', 'AAPL', 'GPRO', 'G', 'INTC', 'SYNC', 'SYNA']
    urls = ["https://finance.yahoo.com/quote/{}".format(ticker) for ticker in tickers]

    loop = asyncio.get_event_loop()
    with aiohttp.ClientSession(loop=loop) as session:
        parsed_data = loop.run_until_complete(parse_urls(session, urls, loop))
        print(parsed_data)