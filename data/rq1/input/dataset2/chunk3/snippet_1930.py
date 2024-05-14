#Source: https://stackoverflow.com/questions/74245441/does-anyone-know-why-i-have-an-attribute-error-on-a-python-discord-bot
import os
import nextcord
import random
from nextcord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', case_insensitive=True, intents=intents)


#when bot joins server console prints
@bot.event
async def on_connect():
  print("Your bot Greg is online!")


#///////////////////////////////////////////////////////////


#commands for bot to follow
@bot.command(name='ping')
async def ping(ctx):
  await ctx.send('pong!')
  await ctx.send('Hi new person!')


#///////////////////////////////////////////////////////////


@bot.command(name='helpc')
async def helpCommand(ctx, *, fromcommands=False):
  if fromcommands(False):
    status = 'did not'
  if fromcommands(True):
    status = 'did'
  print(
    f'{ctx.message.author} asked for help and {status} come from the /commands command.'
  )
  await ctx.send()


#///////////////////////////////////////////////////////////


@bot.command(name='crtchannel',
             description='This is a command for admins to create text channels'
             )
@commands.has_any_role('That_common_coder', 'The creator')
async def create_text(ctx, channel_name='default-bot-name'):
  guild = ctx.guild
  existing_channel = nextcord.utils.get(guild.channels, name=channel_name)

  if not existing_channel:
    print(f'The {channel_name} channel has been created')
    await guild.create_text_channel(channel_name)


#//////////////////////////////
@bot.command(name='commands')
async def commands(ctx):
  await helpCommand(True)


#///////////////////////////////////////////////////////////


@bot.command(
  name='crvchannel',
  description='This is a command for admins to create voice channels')
@commands.has_any_role("That common coder", "The creator")
async def create_voice(ctx, channel_name='default-bot-vc-name'):
  guild = ctx.guild
  existing_channel = nextcord.utils.get(guild.channels, name=channel_name)

  if not existing_channel:
    print(f'This channel: {channel_name} has been created')
    await guild.create_voice_channel(channel_name)


#////////////////////////////////////////////////////////////


@bot.command(name='ban', help='This is the command to ban users')
@commands.has_permissions(ban_members=True)
async def ban_user(ctx, member: nextcord.Member = None, *, reason=None):
  sillyshortword = []
  sillymsg = [
    f'That seems kinda {random.choice(sillyshortword)}',
    f'You are kinda {random.choice(sillyshortword)}', 'You are kinda sussy'
  ]

  #  await user.create_dm()
  #  await message.author.send()
  if member == ctx.message.author:
    print(f'Someone: {ctx.message.author} just tried to ban themself! :)')
    await ctx.send(
      f'You cannot ban yourself, @{ctx.message.author}! :slight_smile:')
    #Note to eli: remember to change this emoji code below
    await member.send(
      f'Why would you try to ban yourself,{ctx.message.author}? :smile:')
    await member.send(sillymsg)
    return
  if member == None:
    print(f'{ctx.message.author} used /ban without any member specified :)')
    await ctx.send(f'{ctx.message.author}, you have to specify a member to ban'
                   )
    return
  if reason == None:
    await member.ban(reason=f'{member} has been banned for (Undefined)')
    await member.send(
      f"You have been banned from {ctx.guild.name}. The result of the ban was unspecified"
    )
  else:
    await member.ban(reason=reason)
    await member.send(
      f"You have been banned from {ctx.guild.name}. The result of the ban was {reason}"
    )
  print(f'{member} has just been banned for {reason}')
  await member.send(f'You have been banned for {reason}')
  await ctx.send(f'{member} has been banned.')


#////////////////////////////////////////////////////////////


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.CheckFailure):
    await ctx.send(
      'Sorry, but you do not have the required roles for this command. ERR 1629'
    )
  else:
    await ctx.send(
      'Sorry, there was an undefined error. This error will soon become specified by the bot owner, and it will have a different response. ERR 16295: UNDEFINED'
    )


#tokens
bottoken = os.environ['token']
bot.run(bottoken)