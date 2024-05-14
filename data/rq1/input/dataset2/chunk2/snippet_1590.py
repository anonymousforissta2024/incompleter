#Source: https://stackoverflow.com/questions/67401599/discord-ext-commands-errors-commandinvokeerror-command-raised-an-exception-typ
import time
from discord.ext import commands

DISCORD_TOKEN = "hahasikeyouwontgetm"

client = commands.Bot(command_prefix="a!")


@client.event
async def on_ready():
    guild_count = 0

    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print("AnythingBot is in " + str(guild_count) + " guilds.")


@client.command()
async def order(ctx, arg):
    if arg == "burger":
        embed = discord.Embed(
            title="here burger",
            color=ctx.author.color
        )
        embed.set_image(url='https://media.discordapp.net/attachments/839166049755856906/839166099336593428/burger.jpg'
                            '?width=670&height=670'
                        )
        await ctx.channel.send(embed=embed)


@client.command()
async def math(ctx, arg, arg2, arg3):
    mathed = 0
    answer = 0
    if arg2 == "+":
        answer = float(arg) + float(arg3)
        mathed = 1
    elif arg2 == "-":
        answer = float(arg) - float(arg3)
        mathed = 1
    elif arg2 == "/":
        answer = float(arg) / float(arg3)
        mathed = 1
    elif arg2 == "*":
        answer = float(arg) * float(arg3)
        mathed = 1
    embed = discord.Embed(
        title="The answer is: " + str(answer),
        color=ctx.author.color
    )
    if mathed == 1:
        await ctx.channel.send(embed=embed)


@client.command()
async def jail(ctx, arg, arg2):
    jailtime = int(arg2) * 60
    arg = arg.replace("<@!", "")
    arg = arg.replace(">", "")
    prisoner = await client.fetch_user(user_id=arg)
    isadmin = False
    admin = discord.utils.get(ctx.guild.roles, name='Admin')
    default = discord.utils.get(ctx.guild.roles, name='Member')
    jailed = discord.utils.get(ctx.guild.roles, name='Jailed')

    embedj = discord.Embed(
        title="Jailed " + prisoner.display_name + " for " + str(jailtime) + "m.",
        color=ctx.author.color
    )

    embedn = discord.Embed(
        title="You must be a staff member to use this command.",
        color=ctx.author.color,
        author="loser"
    )

    embedu = discord.Embed(
        title=prisoner.display_name + " has been unjailed.",
        color=ctx.author.color
    )

    if admin in ctx.message.author.roles:
        if admin in prisoner:
            isadmin = True

        await ctx.channel.send(embed=embedj)
        await client.add_roles(jailed)

        time.sleep(jailtime)

        await ctx.channel.send(embed=embedu)

        if isadmin:
            await client.add_roles(prisoner, admin)
        await client.add_roles(prisoner, default)
    else:
        await ctx.channel.send(embed=embedn)


client.run(DISCORD_TOKEN)