#Source: https://stackoverflow.com/questions/63250747/python3-discord-selfbot-nameerror-name-tokens-is-not-defined
loop = asyncio.get_event_loop()
def Selfbottokens():
    with open("tokens.txt", "r") as f:
        tokens = [token.strip("\n") for token in f.readlines()]
for i in range(len(tokens)):
    client.add_cog(client)
    loop.create_task(client.start(tokens[i], bot=False))