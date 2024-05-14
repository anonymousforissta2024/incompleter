#Source: https://stackoverflow.com/questions/66005708/discord-custom-activity-attribute-error-emoji-object-doesnt-have-attribute-ge
@tasks.loop(seconds=10)
async def change_presence():
    await client.wait_until_ready()
    emoji = client.get_emoji(773100346749878293)
    activity = discord.CustomActivity(name="DMs", type=discord.ActivityType.watching, emoji=emoji)
    await bot.change_presence(status=discord.Status.online, activity=activity)