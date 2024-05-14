#Source: https://stackoverflow.com/questions/65903474/nameerror-name-class-name-is-not-defined-issue
# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# IMPORT THE OS MODULE.
import os
import random
import time
# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands

BMW330i = 'https://automanager.blob.core.windows.net/wmphotos/037685/1844fa46dd334f7dae94afc9ca49aa8a/eaa2cae362_800.jpg'
HONDAs2000 = 'https://cimg3.ibsrv.net/cimg/www.s2ki.com/1600x900_85-1/343/1-Make-Improvements-408343.jpg'
NISSANsilvia ='https://static.carthrottle.com/workspace/uploads/posts/2015/12/9a8cd0a4a74fb73c29f564f6e33aa20f.jpg'

users = 0

class user:
    def __init__(self, name, car, car1,hp, hp1, carc, car1c, cari, car1i, money, daily):
        self.name = name
        self.car = car
        self.car1 = car1
        self.carc = carc
        self.car1c = car1c
        self.hp = hp
        self.hp1 = hp1
        self.money = money
        self.daily = daily
        self.cari = cari
        self.car1i = car1i

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix=";")

@bot.command()
async def test(message):
    p1 = user('imaad', 'd', 'd', 5, 5, 2, 2, 2, 2,2 ,2)
    await message.channel.send(p1.name)
@bot.command()
async def test1(message):
    global p1
    await message.channel.send(p1.name)

@bot.command()
async def reg(cxt):
    global users
    carstart = random.randint(1,3)
    if users == 0:
        await cxt.channel.send('Hey, ' + cxt.author.name)
        if carstart == 1:
            p0 = user(str(cxt.author), '2003 BMW 330i', 'Empty', (235), 'Empty', (9), 'Empty',  BMW330i, 'Empty', (1000), (0))
        if carstart == 2:
            p0 = user(str(cxt.author), '2000 Honda S2000', 'Empty', (240), 'Empty', (9), 'Empty',  HONDAs2000, 'Empty', (1000), (0))
        if carstart == 3:
            p0 = user(str(cxt.author),  '2000 Nissan Silvia', 'Empty', (243), 'Empty', (9), 'Empty',  NISSANsilvia, 'Empty', (1000), (0))
        await cxt.channel.send('Welcome to Brooklyn, ' + p0.name + ' lucky for you I managed to fetch a ' + p0.car + ' with ' + str(p0.hp) + 'HP')
        await cxt.channel.send(p0.cari)
        await cxt.channel.send(p0.name)
        users = users + 1
    else:
        await cxt.channel.send('k')
        




# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run('ODAxODA0NjY0ODM2MDYzMjQy.YAmAyA.snnqa9lOqYheREA0_PqH3GxK94E')