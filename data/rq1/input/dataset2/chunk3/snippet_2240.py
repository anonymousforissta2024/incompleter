#Source: https://stackoverflow.com/questions/66143141/i-have-problem-with-discord-py-typeerror-can-only-concatenate-str-not-float
@client.command(pass_context=True)
async def bitcoin(ctx):
    url = 'http://api.coinlayer.com/live?access_key='
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['rates']['BTC'])