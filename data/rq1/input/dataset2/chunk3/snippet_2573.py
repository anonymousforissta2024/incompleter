#Source: https://stackoverflow.com/questions/63758974/attributeerror-moderation-object-has-no-attribute-channel
import discord
import asyncio
import re
import os
import random
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Purge
    @commands.command()
    async def purge(ctx, amount=10):
        await ctx.channel.purge(limit=amount)
    