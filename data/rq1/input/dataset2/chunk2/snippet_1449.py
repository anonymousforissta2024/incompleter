#Source: https://stackoverflow.com/questions/71310475/typeerror-async-generator-object-is-not-iterable
import asyncio

async def gen_random_numbers():
    for i in range(1, 3):
        await asyncio.sleep(2)
        yield [i for i in range(1, 11)]


async def random_processor():
    async for i, numbers in enumerate(gen_random_numbers()):
        print(f"working with the batch {i}  and processing {numbers}")


asyncio.run(random_processor())