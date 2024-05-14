#Source: https://stackoverflow.com/questions/67428943/understanding-cause-of-an-attributeerror
# bot.py
import discord
from discord import message
import os
import time

client = discord.Client()

msg = message.content
sendmsg = message.channel.send
ss = 'not chanting'

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
  print('I am ready to chant.')

async def chant():
  await asyncio.time(1)
  print('test passed!')
  await sendmsg('passed the test')

async def on_message():
    if msg == '$chant help':
      print('The command \"$chant help\" was called')
      await sendmsg('$chant help - gives a list of commands I can do\n$start chanting - starts chanting in the specified channel\n$stop chanting - stops chanting')

    if ss == 'not chanting':
      if msg == '$start chanting':
        print('The command \"$start chanting\" was called')
        ss = 'chanting'
        await sendmsg('Ok. Chanting now.')
        await sendmsg('reference (this message triggers the code to chant)')

    if ss == 'chanting':
      if msg == '$stop chanting':
        print('The command \"$stop chanting\" was called')
        ss = 'not chanting'
        await sendmsg('Ok. Stopping chanting...')
        await sendmsg('Please wait...')
      
      elif message.user == '{client.user}':
        if msg.contains('reference'):
          chant()

    
client.run('no token 4 u')