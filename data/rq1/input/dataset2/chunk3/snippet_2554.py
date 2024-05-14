#Source: https://stackoverflow.com/questions/77442220/discord-ext-commands-errors-commandinvokeerror-command-raised-an-exception-typ
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def limpar(ctx, ammount):
    await ctx.send(f'{ammount} are going to be deleted')
    sleep(2)
    await ctx.channel.purge(limit=ammount)