#Source: https://stackoverflow.com/questions/67974081/attributeerror-module-embed-storage-has-no-attribute-help-command
import discord
from discord.ext import commands
import gsheet
import os
import embed_storage

async def help(ctx, argument='Helping'):
    await ctx.send(embed=embed_storage.help_command('stargazer', argument))