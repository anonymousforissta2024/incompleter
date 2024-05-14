#Source: https://stackoverflow.com/questions/69509069/getting-typeerror-when-trying-to-log-messages-in-discord
@bot.command()
@commands.has_permissions(administrator = True)
async def logsave(ctx, amount = None, logName = None):
    #Checks if user input an amount, either a number or "all".
    if amount == None:
        desc = f'**Specify an amount**'
        errorEmbed = discord.Embed(title = f'**Log**', description = desc, colour = discord.Color.from_rgb(36, 227, 170))
        await ctx.send(embed = errorEmbed)
        return

    #Checks if user input a name for the log.
    if logName == None:
        desc = f'**Specify a name.**'
        errorEmbed = discord.Embed(title = f'**Log**', description = desc, colour = discord.Color.from_rgb(36, 227, 170))
        logMsg = await ctx.send(embed = errorEmbed)
        return

    #Checks if user input "all"
    if amount.lower() == 'all':
        isAll = True
    else:
        isAll = False

    #Gets message history
    channel = ctx.channel
    if isAll:
        desc = f'**Started Logging**'
        startEmbed = discord.Embed(title = f'**Log**', description = desc, colour = discord.Color.from_rgb(36, 227, 170))
        logMsg = await ctx.send(embed = startEmbed)
        messages = await channel.history(limit = None, oldest_first = True).flatten()
    else:
        messages = await channel.history(limit = int(amount), oldest_first = True).flatten()

    #Loads previous logs for editing
    logsFile = open(f'{currentDirectory}\Saved\logs.json', 'r+')
    logsJson = json.load(logsFile)

    #Creates new message log in JSON
    logCount = logsJson[messages][-1]["count"] + 1
    newLog = {
        "name": logName,
        "creator": ctx.author,
        "msgs": [],
        "count": logCount
    }
    logsJson["messageLogs"].append(newLog)

    #Stars logging the messages, I'm pretty sure this is where my error is coming from.
    for msg in messages:
        msgAuthor = msg.author
        if msgAuthor.bot:
            return
        print("done")
        msgContent = msg.content
        msgAttachments = msg.attachments
        msgCreated = msg.created_at
        msgWrite = f'\n{msgAuthor} [{msgCreated}]\n{msgContent}'
        newMessage = {
            "id": msg.id,
            "authorname": str(msgAuthor),
            "authorid": msgAuthor.id,
            "content": msgWrite,
            "published": msgCreated,
            "attachments": msgAttachments
        }
        logsJson["messageLogs"][logCount]["msgs"].append(newMessage)

    #Edits previous log.
    json.dump(logsJson, logsFile)
    logsFile.close()

    #Ends
    logMsg.delete()
    desc = f'**Finished Logging**'
    endEmbed = discord.Embed(title = f'**Log**', description = desc, colour = discord.Color.from_rgb(36, 227, 170))
    await ctx.send(embed = endEmbed)