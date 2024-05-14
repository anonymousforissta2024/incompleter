#Source: https://stackoverflow.com/questions/71369200/pycord-error-discord-errors-extensionfailed-extension-cogs-cmds-raised-an-er
# main.py

import discord, os, dotenv

# setup
bot = discord.Bot(
    intents = discord.Intents.default(),
    prefix = "zrun "
)

@bot.event
async def on_ready():
    print(f'Connected as {bot.user}')

# load cmds
bot.load_extension('cogs.cmds')

# get token and run bot
dotenv.load_dotenv()
bot.run(os.getenv('TOKEN'))