#Source: https://stackoverflow.com/questions/75982418/attributeerror-module-discord-ui-has-no-attribute-actionrow
# Pin feature
@bot.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == "📌":
        channel = await bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        await message.pin()
    print("Reaction added.")

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.emoji.name == "📌":
        channel = await bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        pins = [reaction for reaction in message.reactions if str(reaction.emoji) == "📌"]
        if len(pins) == 0:
            await message.unpin()
            button = discord.ui.Button(label="View Unpinned Message", style=discord.ButtonStyle.grey, custom_id="view_unpinned_message")
            async def send_message(ctx: discord.Interaction):
                await ctx.channel.send(content=message.content)
            button.callback = send_message
            view_message_action_row = discord.ui.ActionRow(button)
            await channel.send("A previously pinned message has been unpinned.", components=[view_message_action_row])
    print("A reaction has been removed.")