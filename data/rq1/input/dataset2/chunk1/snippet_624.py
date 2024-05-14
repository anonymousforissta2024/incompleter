#Source: https://stackoverflow.com/questions/63027848/discord-py-error-typeerror-new-got-an-unexpected-keyword-argument-deny
import discord
import random
from discord.ext import commands
import asyncio
client = commands.Bot(command_prefix='{')
client.remove_command('help')

@client.event
async def on_ready():
    print("Signed in")

@client.command()
async def dm(ctx):
    await ctx.author.send("What up chump?")

client.run('TOKEN')