#Source: https://stackoverflow.com/questions/66179269/attributeerror-tuple-object-has-no-attribute-set-author-discord-py
@tasks.loop(hours=24)
async def covid_hour():
    channel = client.get_channel(809881992367702117),
    embed = discord.Embed(
        title = "Dane dot. COVID-19 w Polsce:",
        color = discord.Color.blue(),
    ),
    url = 'API'
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed.set_author(name=str(f'{date}'))
        embed.add_field(name='• **Kraj**:', value=str(f"Polska"), inline=False)
        embed.add_field(name='• **Nowe zakażenia**:', value=str(f"{response['dailyInfected']}"), inline=True)
        embed.add_field(name='• **Nowe zgony**:', value=str(f"{response['dailyDeceased']}"), inline=True)
        embed.add_field(name='• **Nowe testy**:', value=str(f"{respons['dailyTested']}"), inline=True)
        embed.add_field(name='• **Nowe uzdrowienia**:', value=str(f"{response['dailyRecovered']}"), inline=True)
        embed.add_field(name='• **Aktualnie zakażonych**:', value=str(f"{respons['activeCase']}"), inline=True)
        embed.add_field(name='• **Łącznie potwierdzonych**:', value=str(f"{response['infected']}"), inline=True)
        embed.add_field(name='• **Łączne zgony**:', value=str(f"{response['deceased']}"), inline=True)
        embed.add_field(name='• **Wyzdrowiałych**:', value=str(f"{response['recovered']}"), inline=True)
        embed.add_field(name='• **Nowych na kwarantannie**:', value=str(f"{response['dailyQuarantine']}"), inline=True)
        embed.set_footer(text="dBot created by Diablo#4700")
        await channel.send(embed=embed)
        #await channel.send('``           ``')