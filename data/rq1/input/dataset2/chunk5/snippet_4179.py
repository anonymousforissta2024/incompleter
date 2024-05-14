#Source: https://stackoverflow.com/questions/55131555/typeerror-not-supported-between-instances-of-member-and-member
d = defaultdict(int)
@bot.event
async def on_message(message):
    d[message.author] += 1
    pass
    await bot.process_commands(message)

@bot.command()
async def top_messager(ctx):
    sorted_d = sorted((value, user) for user, value in d.items())
    await ctx.send('\n'.join(f"{user}: {value}" for value, user in sorted_d))