#Source: https://stackoverflow.com/questions/63288917/discord-py-attributeerror-embed-object-has-no-attribute-get
@commands.command()
async def test(self, ctx, messageID: int):
    channel = self.client.get_channel(740951313482907748)
    
    message = await channel.fetch_message(messageID)
    embed = message.embeds[0]
    embed = discord.Embed.from_dict(embed)
    await ctx.send(embed=embed)