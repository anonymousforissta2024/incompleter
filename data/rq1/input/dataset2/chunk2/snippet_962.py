#Source: https://stackoverflow.com/questions/55593121/typeerror-tuple-indices-must-be-integers-or-slices-not-str-in-command
@checks.can_embed()
@commands.command(name="botinfo")
async def botinfo(self, ctx: UKGCtx):
    """Shows advanced information about the bot."""
    char_count = 0
    deaths_count = 0
    levels_count = 0
    with closing(userDatabase.cursor()) as c:
        c.execute("SELECT COUNT(*) as count FROM chars")
        result = c.fetchone()
        if result is not None:
            char_count = result["count"]
        c.execute("SELECT COUNT(*) as count FROM char_deaths")
        result = c.fetchone()
        if result is not None:
            deaths_count = result["count"]
        c.execute("SELECT COUNT(*) as count FROM char_levelups")
        result = c.fetchone()
        if result is not None:
            levels_count = result["count"]