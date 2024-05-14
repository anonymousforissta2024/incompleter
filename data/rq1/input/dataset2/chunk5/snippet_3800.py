#Source: https://stackoverflow.com/questions/63059165/attributeerror-bot-object-has-no-attribute-pin-message
global stopcheck
stopcheck = 'test'
import asyncio
global time
time = 100
import os
ContinueAutoJoke = 'autojoke'
StopAutoJoke = 'o'
import discord
import time
import random
import discord
from discord.ext import commands



client = discord.Client()
client = commands.Bot(command_prefix = '$')

@client.command()
async def test(ctx):
  message = await ctx.send(f'All messages gonna be deleted in 100 seconds')
  await client.pin_message(message)
  for c in range(-100,0):
      await message.edit(content=f'All messages gonna be deleted in {c} seconds')