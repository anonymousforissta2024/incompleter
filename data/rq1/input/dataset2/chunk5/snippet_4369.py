#Source: https://stackoverflow.com/questions/70644536/how-to-get-around-typeerror-coroutine-object-is-not-callable
def help_utilities(ctx):
    embed = discord.Embed(
        color=discord.Colour.dark_blue()
    )
    embed.set_author(name="help utils")
    embed.add_field(name="Decode", value="Decodes an encrypted message (Base64)")
    embed.add_field(name="Encode", value="Encodes a message in base64")
    embed.add_field(name='Embed', value='Speak through the bot, but with fancy text"', inline=False)
    embed.add_field(name="Add/Subtract/Multiply/Divide", value="Just take two values and do whatever operation with them", inline=False)
    embed.add_field(name="Reverse", value="Reverses your text :/", inline=False)
    embed.add_field(name='Say', value='Speak through the bot!', inline=False)
    author = ctx.message.author
    author.send(embed=embed)

@client.command(pass_context=True)
async def help(ctx, arg=None):
    author = ctx.message.author

    if arg is None:
        embed = discord.Embed(
            color=discord.Colour.gold()
        )
        embed.set_author(name='Help')
        embed.add_field(name="Invite", value="Sends the invite url of the bot lmao", inline=False)
        embed.add_field(name="Disclaimer", value="for the commands below you need to call them like this: .mod \n Basically the second word :sleepy:")
        embed.add_field(name="help mod", value="To see more info on my moderation commands", inline=False)
        embed.add_field(name="help utils", value="To see more info on my utility commands", inline=False)
        embed.add_field(name="help fun", value="My more fun commands :eyes:", inline=False)
        await author.send(embed=embed)
    if (arg == "utils") or (arg == "Utils"):
        help_utilities()
   # there are more If statments like this but right now I will only focus on 1
   # So you can get the idea of whats going on
    else:
        await ctx.send("bro thats not a valid argument")