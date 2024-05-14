#Source: https://stackoverflow.com/questions/59754188/getting-attribute-error-module-mod-commands-has-no-attribute-ban-even-tho
import mod_commands
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='~',description=description)

@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, members : commands.Greedy[discord.Member], *, reason = 'Idiotisches Verhalten'):
    await mod_commands.ban(ctx, members, reason)

def getLatency():
    return bot.latency

bot.run(TOKEN)