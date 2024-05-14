#Source: https://stackoverflow.com/questions/66898793/discord-py-attributeerror-context-object-has-no-attribute-reference
@bot.command(brief="Iri? Bilang Bos!", description="Iri? Bilang Bos!")
async def iri(ctx):
    ref = ctx.reference
    x=['https://i.imgur.com/8mfw6Nv.jpg', 'https://tenor.com/view/iri-bilang-bos-spell-power-up-skill-gif-17176211', 'https://i.imgur.com/hOvruLZ.jpg']
    await ctx.delete()
    await ctx.send(random.choice(x), reference=ref)