#Source: https://stackoverflow.com/questions/63565924/typeerror-module-object-is-not-callable-discord-py
import discord
from discord.ext.commands import Bot
from discord.ext import commands

client = commands.bot(command_prefix = ".")

@client.event
async def on_ready():
    print("I'm in!")


@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
       return
    
    if message.content.startswith("hello"):
        await message.channel.send('hello!')

@client.event
async def on_member_join(member):
    print("someone's here!")


@client.event
async def on_typing(channel, user, when):
    print("Lol, someone is typing!!1!")

@client.command()
async def answer(ans):
    await ans.send("Here is your answer")