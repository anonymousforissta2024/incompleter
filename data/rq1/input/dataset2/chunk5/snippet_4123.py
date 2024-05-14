#Source: https://stackoverflow.com/questions/62286462/error-command-raised-an-exception-typeerror-nonetype-object-is-not-subscr
@client.command()
async def anime(ctx):
    await ctx.send("Récupération d'un anime...")
    anime = 0
    while anime == 0:
        async with ctx.typing():
            try:
                ref = randrange(1, 40500)
                anime = Anime(ref)
                await ctx.send(anime)
            except ValueError as err:
                if str(err) == 'No such id on MyAnimeList':
                    pass
                else:
                    pass