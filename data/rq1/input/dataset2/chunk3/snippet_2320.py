#Source: https://stackoverflow.com/questions/67911019/discord-py-blacklist-cog-listener-flagging-error-typeerror-str-object-not-c
@commands.Cog.listener()
async def on_message(self, message):
    """Deletes a messaged that contains a blacklisted word"""

    msg = message.content()

    for word in msg:

        if msg.find("blacklist") != -1:

            await message.delete()