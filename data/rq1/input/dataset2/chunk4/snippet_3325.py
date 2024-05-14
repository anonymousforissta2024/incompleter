#Source: https://stackoverflow.com/questions/66663801/errorhandling-indexerror-and-attribute-error-with-discordpy
@redditsearch.error
async def redditsearch_error(ctx, inst):
    if isinstance (inst, IndexError):
        await ctx.send(f"Exception raised. This probably means I failed to find an image.")
    else:
        await ctx.send(f"Exception raised. \n\n{inst}")