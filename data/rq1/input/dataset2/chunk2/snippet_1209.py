#Source: https://stackoverflow.com/questions/65002409/typeerror-event-registered-must-be-a-coroutine-function-discord-py
@client.event
async def on_ready():
    change_status.start()
    print('Bot is online')



@tasks.loop(seconds=3600)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))



@client.event
def on_guild_join(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)


    prefixes[str(message.guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)



@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)


    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)



@client.command(pass_context = True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)


    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)