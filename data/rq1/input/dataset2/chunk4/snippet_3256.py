#Source: https://stackoverflow.com/questions/63638458/typeerror-init-got-an-unexpected-keyword-argument-after
voice.play(discord.FFmpegPCMAudio(audio, after=lambda e: looptrack(ctx)))