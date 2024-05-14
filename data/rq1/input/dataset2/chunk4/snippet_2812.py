#Source: https://stackoverflow.com/questions/67491060/beginner-discord-bot-problems-attributeerror-nonetype-object-has-no-attrib
import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix='$')
intents = discord.Intents().all()
TOKEN = 'changeditforexample'

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.command(name='server')
async def fetchserverInfo(ctx):
    guild = ctx.guild

    await ctx.send(f'Server Name: {guild.name}')
    await ctx.send(f'Server Size: {len(guild.members)}')
    await ctx.send(f'Server owner: {guild.owner.display_name}')


bot.run(TOKEN)