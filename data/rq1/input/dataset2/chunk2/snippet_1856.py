#Source: https://stackoverflow.com/questions/65002409/typeerror-event-registered-must-be-a-coroutine-function-discord-py
import discord, asyncio, time, discord.guild, random, os, youtube_dl
import os
import asyncio
import math
import random
import youtube_dl
import json
from discord.ext import commands, tasks
from discord.ext.commands import Bot, guild_only
from itertools import cycle


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)


        return prefixes[str(message.guild.id)]