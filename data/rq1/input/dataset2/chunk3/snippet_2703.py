#Source: https://stackoverflow.com/questions/66076831/discord-py-music-bot-raising-typeerror-when-a-youtube-link-is-given-in-the-play
class MusicSource(discord.PCMVolumeTransformer):
    youtube_dl.utils.bug_reports_message = lambda: ''  # Suppressing Random Youtube_Dl warnings
    ytdl_format_options = {  # options for the youtube_dl module, for the audio quality
        'format': 'bestaudio/best',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'ytsearch',  # We will use Youtube for searching musics
        'source_address': '0.0.0.0',  # IPv6 causes problem sometimes so we are using IPv4
        'youtube_include_dash_manifest': False  # Turning off dash manifest
        # (Enabling it sometimes makes the bot not play anything)
    }
    ytdl = youtube_dl.YoutubeDL(ytdl_format_options)  # Sending the options to the Youtube_DL class

    def __init__(self, source: discord.AudioSource, *, data):
        self.volume = 0.4
        super().__init__(source, self.volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')
        self.link = data.get('webpage_url')  # Fetching the youtube link for the song and
        # will be used later for sending it to the user
        self.time = data.get('duration')
        self.img = data.get('thumbnail')
        self.artist = data.get('artist')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.albm = data.get('album')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False, timestamp=0):  # The player that plays the
        # audio from the url
        ffmpeg_options = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': f'-vn -ss {timestamp}'
        }
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: cls.ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]  # Taking the first item from the search results
            filename = data['url'] if stream else cls.ytdl.prepare_filename(data)
            return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)