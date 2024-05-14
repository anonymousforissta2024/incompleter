#Source: https://stackoverflow.com/questions/52356984/discord-py-attributeerror-context-object-has-no-attribute-server
@commands.command(pass_context=True, no_pm=True)                
async def unpin(self, ctx):
    """Listen for a message then unpin any other messages older than 7 days"""
    server = ctx.server
    messages = await self.bot.pins_from(self.bot.get_channel('490899209067823135'))
    if server:
        for msg in messages:
            if (datetime.now() - msg.timestamp).days > 7:
                try:
                   await self.bot.unpin_message(msg)
                   print ("Unpinned")

                except discord.Forbidden:
                   print("No permissions to do that!")