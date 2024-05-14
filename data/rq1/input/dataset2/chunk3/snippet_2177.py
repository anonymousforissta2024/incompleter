#Source: https://stackoverflow.com/questions/62396146/discord-py-osu-stats-error-command-raised-an-exception-typeerror-list-indices
@client.command()
async def osu(ctx, arg):
    token = "secret token"
    res = requests.get(f"https://osu.ppy.sh/api/get_user?u={arg}&k={token}")

    nickname = res.json()['username']

    embed = discord.Embed(title="Ecco le statistiche di osu.", description=f'Speriamo sia forte lmao', color=discord.Color.orange())
    embed.add_field(name="Nickname", description=nickname)

    await ctx.send(embed=embed)