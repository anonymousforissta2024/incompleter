#Source: https://stackoverflow.com/questions/52245947/typeerror-list-iterator-object-is-not-async-iterable
import requests as req
from bs4 import BeautifulSoup as bs
import os
import asyncio
from aiostream import stream, pipe

myList = []

def get_myList():
    """
    Append values to myList in the format [(,), (,), (,), ...]
    """

async def download(link, title):

    # Download a page
    try:
        page = await req.get(link)
        # Process with BeautifulSoup
        pass
    except:
        pass

async def main():
    get_myList()

    min_iterList = iter(myList[:])

    stream.starmap(min_iterList, download, ordered=True, task_limit=10)

if __name__=="__main__":
    freeze_support()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()