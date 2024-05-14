#Source: https://stackoverflow.com/questions/67059050/typeerror-init-takes-1-positional-argument-but-2-were-given-announcemen
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = "+")
client.remove_command("help")

@client.event
async def on_ready():
   print(client.user.name)
   print("Online")
   print("-------")

@client.command(pass_context=True)
async def announce(ctx,*,message):
    embed = discord.Embed("Information",description=message,color=0x9200ea)
    embed.set_footer(text="Made by Elanovic#7940")
    await client.send_message(ctx.message.channel,embed=embed)

client.run("TOKEN")