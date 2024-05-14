#Source: https://stackoverflow.com/questions/68582138/typeerror-on-voice-state-update-takes-3-positional-arguments-but-4-were-given
import discord
from discord.ext import commands
from pymongo import MongoClient
# from discord_components import DiscordComponents, Button, ButtonStyle
from datetime import datetime
import time
import os


client = commands.Bot(command_prefix = "!")
cluster = MongoClient("mongodb://127.0.0.1:27017")
colluser = cluster.chill.user
collclan = cluster.chill.clans
collshop = cluster.chill.shop


@client.event
async def on_ready():
    # DiscordComponents(client)
    print("Bot connected to the server")
    # post2 = {

    # }

    for guild in client.guilds:
        for member in guild.members:
            post = {
                "_id": member.id,
                "name": member.mention,
                "user": member.name,
                "inventory": [],
                "warms": 0,
                "mute": 0,
                "voice_activ": 0,
                "localban": 0,
                "register": member.created_at,
                "onservfrom": member.joined_at,
                "clan": 0,
                "marry": 0,
                "love": 0,
                "childs": [],
                "balance": 0,
                "bank": 0,
                "rep": 0,
                "cdxp": 0,
                "cnxp": 0,
                "dxp": 0,
                "nxp": 0,
                "cdbal": 0,
                "cdlvl": 1,
                "cnlvl": 1,
                "dlvl": 1,
                "nlvl": 1
            }

            if colluser.count_documents({"_id": member.id}) == 0:
                colluser.insert_one(post)

@client.event
async def on_guild_role_create(role):
    print("new role created")
    # print(f"{role.id}")
    # print(f"{role.name}")
    post = {
        "_id": role.id,
        "titel": "none",
        "cp": [],
        "exp": 0,
        "lvl": 0,
        "maxcp": 7,
        "bank": 0
    }

    if collclan.count_documents({"role_id": role.id}) == 0:
        collclan.insert_one(post)

@client.event
async def on_voice_state_update(member, before, after):
    data = colluser.find_one({"_id": member.id})
    day = data["dxp"]
    dark = data["nxp"]
    dl = data["dlvl"]
    nl = data["nlvl"]
    dexp = 500 + 100 * dl
    nexp = 500 + 100 * nl
    if before.channel is None and after.channel is not None:
        print("1")
        t1 = time.time()
        colluser.update_one({"_id": member.id},
            {"$set": {"voice_tim1": t1}})
    elif before.channel is not None and after.channel is None:
        dtn = datetime.today().strftime("%I:%M %p")
        t1 = data["voice_tim1"]
        voice_activ1 = data["voice_activ"]
        balance = data["balance"]
        t2 = time.time()
        tim = t2-t1
        print("0")
        print(dtn)
        colluser.update_one({"_id": member.id},
            {"$set": {"voice_activ": voice_activ1 + tim}})
        colluser.update_one({"_id": member.id},
            {"$set": {"balance": balance + tim / 30}})
        if any(("AM" in dtn) for AM in dtn):
            print("time is AM")
            colluser.update_one({"_id": member.id},
                {"$set": {"dxp": day + tim / 4}})
        if any(("PM" in dtn) for PM in dtn):
            print("time is PM")
            colluser.update_one({"_id": member.id},
                {"$set": {"nxp": dark + tim / 4}})
        if data["dxp"] >= 500 + 100 * dl:
            colluser.update_one({"_id": member.id},
                {"$set": {"dlvl": dl + 1}})
            colluser.update_one({"_id": member.id},
                {"$set": {"dxp": day - dexp}})
        if data["nxp"] >= 500 + 100 * nl:
            colluser.update_one({"_id": member.id},
                {"$set": {"nlvl": nl + 1}})
            colluser.update_one({"_id": member.id},
                {"$set": {"nxp": dark - nexp}})


@client.event
async def on_member_join(member):
    post = {
        "_id": member.id,
        "name": member.mention,
        "user": member.name,
        "inventory": [],
        "warms": 0,
        "mute": 0,
        "voice_activ": 0,
        "localban": 0,
        "register": member.created_at,
        "onservfrom": member.joined_at,
        "clan": 0,
        "marry": 0,
        "love": 0,
        "childs": [],
        "balance": 0,
        "bank": 0,
        "xp": 0,
        "dxp": 0,
        "nxp": 0,
        "cdbal": 0,
        "lvl": 1,
        "dlvl": 1,
        "nlvl": 1
    }

    if colluser.count_documents({"_id": member.id}) == 0:
        colluser.insert_one(post)


@client.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.UserInputError):
        await ctx.send(embed = discord.Embed(
            description = f"Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief}): `{ctx.prefix}{ctx.command.usage}`"
        ))


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run("TOKEN")