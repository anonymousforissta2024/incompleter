#Source: https://stackoverflow.com/questions/70186078/typeerror-event-missing-1-required-positional-argument-coro
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
from config import  token

import  youtube_dl
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('bot online!')

@bot.event()
async def on_message():
    print('New Message!')

bot.run(token)