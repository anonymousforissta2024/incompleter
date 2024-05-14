#Source: https://stackoverflow.com/questions/59754188/getting-attribute-error-module-mod-commands-has-no-attribute-ban-even-tho
import discord
import programm

def createEmbed(guild, title, description, colour : discord.colour):
    embed = discord.Embed(title = title, description=description, colour=colour)
    embed.set_footer(text=guild.name + '||%.2fs' % programm.getLatency(), icon_url=guild.icon_url)
    embed.type = 'rich'
    return embed