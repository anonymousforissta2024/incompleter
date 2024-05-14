#Source: https://stackoverflow.com/questions/66187544/discord-py-covid-module-doesnt-work-attributeerror-extra-no-attribute-allow
@tasks.loop(hours=24)
async def covid_hour():
    channel = client.get_channel(809881992367702117)
    embed = discord.Embed(
        title = "Dane dot. COVID-19 w Polsce:",
        color = discord.Color.red()
    )
    url = 'API'
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed.set_author(name=str(f'{date}'))
        embed.add_field(name='• **Kraj**:', value=str(f"Polska"), inline=False)
        embed.add_field(name='• **Nowe zakażenia**:', value=str(f"{response['dailyInfected']}"), inline=True)
        embed.set_footer(text="dBot created by Diablo#4700")
        await channel.send(embed=embed)
        #await channel.send('``           ``')