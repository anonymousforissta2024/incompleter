#Source: https://stackoverflow.com/questions/65946763/attributeerror-str-object-has-no-attribute-get-in-discord-bot
@bot.command()
async def bestPct(ctx, firstName=None, lastName=None, server=None, region=None):
    if all([firstName, lastName, server, region]):
        message = fflogs_request.best_percentile_of("{} {}".format(firstName, lastName), server, region)
    else:
        message = """Usage: !bestPct <firstName> <lastName> <server> <region>"""
    await ctx.channel.send(message)