#Source: https://stackoverflow.com/questions/71498995/discord-python-error-typeerror-unhashable-type-list
import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
discord.members = True
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)

@client.command()
async def highLow(ctx: commands.Context):
    AceCard = [1]
    TwoCard = [2]
    ThreeCard = [3]
    FourCard = [4]
    FiveCard = [5]
    SixCard = [6]
    SevenCard = [7]
    EightCard = [8]
    NineCard = [9]
    TenCard = [10]
    JackCard = [11]
    QueenCard = [12]
    KingCard = [13]
    randomCard = random.choice({AceCard}, {TwoCard}, {ThreeCard}, {FourCard}, {FiveCard}, {SixCard}, {SevenCard}, {EightCard}, {NineCard}, {TenCard}, {JackCard}, {QueenCard}, {KingCard})
    embed = discord.Embed(title="Welcome to HighLow", description=f"You have {randomCard}", colour=0x87CEEB)
    embed.set_author(name="Anwais#6857")
    embed.add_field(name="Higher", value="React 1 for higher", inline=False)
    embed.add_field(name="Lower", value="React 2 for lower", inline=True) 
    global one
    one = client.get_emoji(946853495628238878)
    global two
    two = client.get_emoji(946853495716327504)
    messageBeforeCard1 = await ctx.channel.send(embed=embed)
    await messageBeforeCard1.add_reaction(one)
    await messageBeforeCard1.add_reaction(two)
    print("a")
    
@client.event
async def on_reaction_add(reaction, user, ctx: commands.Context):
        one= 1
        HigherLowerId = 0
        oneReaction = 0
        twoReaction = 0
        if reaction.emoji.id == one:
            if user.id == HigherLowerId :
                await ctx.send(f"You chose {one}")
                
            else:
                await reaction.message.channel.send(f"This is not your game, {user.mention}")
        elif reaction.emoji.id != oneReaction:
            pass 