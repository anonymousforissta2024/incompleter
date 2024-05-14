#Source: https://stackoverflow.com/questions/70618400/typeerror-greedystr-is-invalid-discord-py
@commands.command()
async def temp(self, ctx: commands.Context, *arg):
    user_id = re.findall(r'(?<=<@)[!&]?(\d{17,22})(?=> *$)', arg[-1])
    if len(user_id ) == 0:
      raise TypeError('Command "temp" missing 1 required positional argument: "user"')
    user = ctx.guild.get_member(int(user_id[0]))
    message = ' '.join(arg[:-1])
    await ctx.send(f'{message = }, {user.mention}')