#Source: https://stackoverflow.com/questions/66274519/attributeerror-str-object-has-no-attribute-get-discord-py
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
Bot = commands.Bot(command_prefix="&", intents=intents)

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Activity(type=4, emoji="😁", name="hello")) # The error is related to this line
    print("ready!")

Bot.run(TOKEN)