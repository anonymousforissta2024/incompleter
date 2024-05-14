#Source: https://stackoverflow.com/questions/71369200/pycord-error-discord-errors-extensionfailed-extension-cogs-cmds-raised-an-er
# cogs/cmds.py

import discord
from discord.ext import commands

class Cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, msg:str):
        """Sends the specified text in the chat"""

        await ctx.send(msg)

def setup(bot):
    bot.add_cog(Cmds(bot))