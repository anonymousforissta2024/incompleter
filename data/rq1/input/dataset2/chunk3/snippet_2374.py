#Source: https://stackoverflow.com/questions/76367183/command-reload-raised-an-exception-typeerror-botbase-reload-extension-miss
import discord
import settings

from discord.ext import commands
from discord.interactions import Interaction

@commands.hybrid_command(name="reload", description="Reloads all extensions")
async def reload(ctx):
     for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                extensions = f"extension.{cmd_file.name[:-3]}"
                await commands.Bot.reload_extension(name=extensions)
                print(f"Reloaded extension: {extensions}")

async def setup(bot):
    bot.add_command(reload)