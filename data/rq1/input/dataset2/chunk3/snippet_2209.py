#Source: https://stackoverflow.com/questions/70113301/typeerror-module-object-is-not-callable-on-discord-py
from discord.ext import commands

token = 'token goess here'

client = commands.bot(command_prefix = '__')

@client.event
async def on_ready():
    print('Bot is ready')

client.run(token)