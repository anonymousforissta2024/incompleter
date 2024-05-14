#Source: https://stackoverflow.com/questions/70428799/discord-py-musicbot-gives-nonetype-error
@commands.command()
async def join(self,ctx):
    if ctx.author.voice is None:
        await ctx.send("Du bist in keinem VC!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)
@commands.command()
async def stop(self,ctx):
    await ctx.voice_client.disconnect()

@commands.command()
async def play(self,ctx,url):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_Options) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2,
        **FFMPEG_OPTIONS)
        vc.play(source)

@commands.command()
async def pause(self,ctx):
    await ctx.voice_client.pause()
    await ctx.send("Pausiert")

@commands.command()
async def resume(self,ctx):
    await ctx.voice_client.resume()
    await ctx.send("wird Weitergespielt...")