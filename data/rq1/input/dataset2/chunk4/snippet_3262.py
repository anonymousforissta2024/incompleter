#Source: https://stackoverflow.com/questions/70917965/attributeerror-interaction-object-has-no-attribute-author
@bot.slash_command(name='credits', description='Checks social credit score', guild_ids=guild_id)
async def creds(message):
    member_data = load_member_data(message.author.id)
    await message.channel.send(f"{message.author.mention} has "+ str(member_data.wallet) +" Social Credit Points")