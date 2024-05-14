#Source: https://stackoverflow.com/questions/73310014/command-raised-an-exception-attributeerror-nonetype-object-has-no-attribute
@client.command()
@commands.has_role(MANAGEMENT_ROLE_ID)
async def archive(ctx: commands.Context): 
    transcript = await chat_exporter.export(
        ctx.channel,
        tz_info="UTC",
        military_time=True, 
        bot=client
        )

    if transcript is None:
        return

    print(transcript)
    transcript_file = discord.File(
        io.BytesIO(transcript.encode()),
        filename=f"transcript-{ctx.channel.name}",
    )

    await ctx.send(file=transcript_file)