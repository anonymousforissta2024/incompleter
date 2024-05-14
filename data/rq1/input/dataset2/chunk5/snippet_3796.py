#Source: https://stackoverflow.com/questions/59502253/i-cant-use-bot-commands-and-typeerror-property-object-is-not-callable
manage.py

import discord
import asyncio
import re
import json
from discord.ext import commands
from discord import Permissions as permissions

class manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @permissions.administrator()
    async def prefix(self, ctx, *, prefixes=""):
        try:
            with open('config/setting.json') as json_file:
                json_data = json.load(json_file)
                prefix = json_data["prefix"]
        except:
            await ctx.send("An error occured.(Bot has an error.)")
        if(prefixes != ""):
            try:
                custom_prefixes = prefixes
                custom_prefixes[ctx.guild.id] = prefixes.split() or prefix
                await ctx.send("Changed prefix. Now new prefix is **{}**.".format(custom_prefixes))
            except:
                await ctx.send("An error occured.(Check your command or bot has an error.)")
def setup(bot):
    bot.add_cog(manage(bot))