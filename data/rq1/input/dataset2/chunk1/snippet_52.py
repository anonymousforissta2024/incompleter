#Source: https://stackoverflow.com/questions/70618400/typeerror-greedystr-is-invalid-discord-py
@commands.command()
async def temp(self, ctx:commands.Context, message:commands.Greedy[str]='None', user:discord.Member=None):
    await ctx.send(f'{message = }, {user.mention}')