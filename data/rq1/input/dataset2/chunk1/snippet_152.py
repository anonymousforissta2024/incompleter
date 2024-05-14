#Source: https://stackoverflow.com/questions/53247533/attributeerror-module-asyncio-has-no-attribute-create-task
async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(async_say(4, 'hello'))
    task2 = loop.create_task(async_say(6, 'world'))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())