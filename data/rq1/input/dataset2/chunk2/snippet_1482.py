#Source: https://stackoverflow.com/questions/53999771/discord-py-bot-rewrite-attributeerror-bot-object-has-no-attribute-send-messa
from discord.ext.commands import Bot
import os

BOT_PREFIX = ("?")
access_token= os.environ["ACCESS_TOKEN"]

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
     if message.content.startswith("?"):
         newMessage = 'text' + str(message.content)[1:].upper() + '.png'
         await client.send_message(message.channel, newMessage)

client.run(access_token)