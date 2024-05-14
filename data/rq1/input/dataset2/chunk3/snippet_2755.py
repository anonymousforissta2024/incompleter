#Source: https://stackoverflow.com/questions/65814425/discords-new-support-for-slash-commands-attributeerror-with-discord-py-slash
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot)


@slash.slash(name="test")
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])




bot.run(".token.txt")