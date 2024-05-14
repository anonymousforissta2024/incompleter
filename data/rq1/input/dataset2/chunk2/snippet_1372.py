#Source: https://stackoverflow.com/questions/59754188/getting-attribute-error-module-mod-commands-has-no-attribute-ban-even-tho
import bot_utility
from discord.ext import commands

async def ban(ctx, members, reason):
    print('command => mod_commands.ban')
    bannableMembers = []
    for member in members:
        if(member.guild_permissions.administrator):
            await ctx.send('{} kann nicht gebannt werden.'.format(member.display_name))
        else:
            bannableMembers.append(member)
            embed = bot_utility.createEmbed(ctx.guild, 'Du wurdest gebannt', 'Grund: ' + reason, 0xFF0000)
            await member.send(embed=embed)
            await ctx.guild.ban(member, reason=reason)
    if(bannableMembers != None):
        embed = bot_utility.createEmbed(ctx.guild, 'Banns: (' + str(len(bannableMembers)) + ')', 'Grund: ' + reason, 0xff0000)
        for member in bannableMembers:
            embed.add_field(name=member.display_name, value=member.id)
        await ctx.send(embed=embed)