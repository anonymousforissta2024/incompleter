#Source: https://stackoverflow.com/questions/56369406/discord-bot-attributeerror-client-object-has-no-attribute-commands
import discord
import asyncio 
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = [REDACTED]



# client = discord.Client()

client = Bot("!")

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        @client.command(pass_context=True)
        async def broadcast(ctx, *, msg):
                for server in bot.guilds:
                    for channel in server.channels:
                        try:
                            await channel.send(msg)
                        except Exception:
                            continue
                        else:
                            break