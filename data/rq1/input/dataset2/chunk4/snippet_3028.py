#Source: https://stackoverflow.com/questions/73074930/nameerror-name-aiter-is-not-defined
async def numbers(num):
    for i in range(num):
        yield i
        await asyncio.sleep(0.5)

async def check_odd(num):
    it = aiter(numbers(num))
    while True:
        x = await anext(it, 'end')
        if x == 'end':
            break
        elif x % 2 != 0:
            print(f"{x} is Odd!!")

if __name__ == " __main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(check_odd(10))
    finally:
        event_loop.close()

nest_asyncio.apply()
asyncio.run(check_odd(10))