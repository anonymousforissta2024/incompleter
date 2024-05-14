#Source: https://stackoverflow.com/questions/73307348/typeerror-export-got-an-unexpected-keyword-argument-set-timezone
@client.command()
@commands.has_role(MANAGEMENT_ROLE_ID)
async def archive(channel, archive_channel):
        if channel and archive_channel:
            transcript = await chat_exporter.export(channel, set_timezone='UTC')
            transcript_file = discord.File(io.BytesIO(transcript.encode()), filename=f"{channel.name}.html")
            await archive_channel.send(file=transcript_file)