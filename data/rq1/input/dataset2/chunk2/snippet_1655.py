#Source: https://stackoverflow.com/questions/68431205/typeerror-asyncio-runners-run-argument-after-must-be-an-iterable-not-corou
f = open("tokens.txt", "r")
lines = f.readlines()
for line in lines:
    print(type(line), line)


async def hosting(token): 

        bot = discord.Client()
        await bot.login(token)
        print(f"Connected as: {token}")

async def do_something_important():
    await print(10)


if __name__ == "__main__":

  for token in lines:
    _thread = threading.Thread(target=asyncio.run, args=(hosting(token)))
    _thread.start()
 