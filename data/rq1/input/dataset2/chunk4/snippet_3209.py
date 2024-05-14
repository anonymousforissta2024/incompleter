#Source: https://stackoverflow.com/questions/73551025/discord-py-self-aftererror-typeerror-lambda-takes-0-positional-arguments
players = {}
queues = {}

class music(commands.Cog):
  def __init__(self, client):
    self.client = client

  def queueCheck(self, id, vc):
    if queues[id] != []:      # if server queue not empty
      stream = queues[id].pop(0, None)
      players[id] = stream
      vc.play(stream)

  

  async def playSong(self, ctx, url):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio",
                    'default_search':'auto'}
    
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      if 'entries' in info:        # if no url is input
        url2 = info['entries'][0]['formats'][0]['url']
      elif 'formats' in info:      # if url is passed
        url2 = info['formats'][0]['url']
      stream = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)

    return stream
  
  @commands.command()
  async def play(self, ctx, *, url):
    if ctx.voice_client is None:
      await ctx.author.voice.channel.connect()

    stream = await self.playSong(ctx, url)
    guild = ctx.message.guild
    vc = ctx.voice_client
    players[guild.id] = stream
    vc.play(stream, after=lambda: self.queueCheck(guild, vc))
    

  @commands.command()
  async def queue(self, ctx, url):
    guild = ctx.message.guild
    stream = await self.playSong(ctx, url)

    if guild.id in queues:
      queues[guild.id].append(stream)
    else:
      queues[guild.id] = [stream]

    await ctx.send("Song queued.")
  