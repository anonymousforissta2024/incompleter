#Source: https://stackoverflow.com/questions/66922980/discord-py-few-tasks-working-some-not-attributeerror-nonetype-object-has-no
@online_stats.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")