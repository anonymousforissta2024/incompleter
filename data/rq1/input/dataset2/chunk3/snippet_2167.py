#Source: https://stackoverflow.com/questions/66144895/discord-bot-problem-discord-py-attributeerror-bot-object-has-no-attribute-c
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    crypto_hour.start()
    print('Bot is active!')

@tasks.loop(hours=10)
async def crypto_hour():
    channel = bot.get_channel(809155804170682408)
    embed = discord.Embed(
        title = ":D",
        color = discord.Color.blue(),
    )
    url = 'http://api.coinlayer.com/live?access_key='
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed.set_author(name=':D')
        embed.add_field(name='• **Bitcoin (BTC)**:', value=str(f"{response['rates']['BTC']}PLN"), inline=True)
        embed.add_field(name='• **Ethereum (ETH)**:', value=str(f"{response['rates']['ETH']}PLN"), inline=True)
        await bot.channel.send(embed=embed)