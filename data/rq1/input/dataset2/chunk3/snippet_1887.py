#Source: https://stackoverflow.com/questions/51988684/discord-py-when-creating-group-gives-attributeerror
# reddit group commands
@function_debug
@bot.group(pass_context = True)
async def reddit(context):
    message = context.message
    logger.debug(message.content)
    try:
        if message.server.name == 'PeaceCrafters' and message.channel.name == 'utilbots':
            cont = True
        elif message.server.name != 'PeaceCrafters':
            cont = True
        else:
            cont = False
    except AttributeError:
        cont = True
    finally:
        if cont:
            if context.invoked_subcommand is None:
                await reddit_help()


@function_debug
@reddit.command(name = 'help', description = 'Provides help with reddit', pass_context = True)
async def reddit_help(context):
    message = context.message
    logger.debug(message.content)
    try:
        if message.server.name == 'PeaceCrafters' and message.channel.name == 'utilbots':
            cont = True
        elif message.server.name != 'PeaceCrafters':
            cont = True
        else:
            cont = False
    except AttributeError:
        cont = True
    finally:
        if cont:
            message = reddit_message
            await bot.say(message)


@function_debug
@reddit.group(pass_context = True)
async def subreddit(context):
    message = context.message
    logger.debug(message.content)
    try:
        if message.server.name == 'PeaceCrafters' and message.channel.name == 'utilbots':
            cont = True
        elif message.server.name != 'PeaceCrafters':
            cont = True
        else:
            cont = False
    except AttributeError:
        cont = True
    finally:
        if cont:
            info = message.content.split(' ')[1:]
            subreddit = info[0]

@function_debug
@subreddit.command(name = 'hot', description = 'Lists the hot commands in the subreddit', pass_context = True)
async def subreddit_hot(context):
    message = context.message
    logger.debug(message.content)
    try:
        if message.server.name == 'PeaceCrafters' and message.channel.name == 'utilbots':
            cont = True
        elif message.server.name != 'PeaceCrafters':
            cont = True
        else:
            cont = False
    except AttributeError:
        cont = True
    finally:
        if cont:
            pass #i will add more once i figure out how message.content is handled