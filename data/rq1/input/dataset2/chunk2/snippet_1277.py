#Source: https://stackoverflow.com/questions/62250609/attributeerror-levelingsystem-object-has-no-attribute-author
import discord
from discord.ext import commands
from discord.utils import get
import json
import random
import time


class LevelingSystem(commands.Cog):
    """ Leveling system for discord """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(message, guild):

        if message.author.bot:
            return
        else:
            with open("X:\\Code\\Projects\\Python\\AlphaWolf\\cogs\\levels.json", 'r') as f:
                levels = json.load(f)

            await update_data(levels, message.author.id)

        async def update_data(levels, user):
            for member in guild.members:
                if user not in levels:
                    levels[user] = {}
                    levels[user]["experience"] = 0
                    levels[user]["level"] = 1
                    print(" Registered {} to .json".format(user))
                    with open("X:\\Code\\Projects\\Python\\AlphaWolf\\cogs\\levels.json", 'w') as f:
                        json.dump(levels, f)

def setup(bot):
    bot.add_cog(LevelingSystem(bot))