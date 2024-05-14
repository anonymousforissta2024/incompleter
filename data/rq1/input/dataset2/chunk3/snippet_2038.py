#Source: https://stackoverflow.com/questions/73349559/ctx-player-ctx-attributeerror-player-object-has-no-attribute-ctx
import wavelink
import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix='>>')


@bot.event
async def on_ready():
    print('Bot Online')
    bot.loop.create_task(node_connect())


@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f'Node <{node.identifier}> is ready')


async def node_connect():
    await bot.wait_until_ready()
    await wavelink.NodePool.create_node(bot=bot, host='ash-01.thermalhosting.com', port=2008, password='ASH-01')


@bot.event
async def on_wavelink_track_end(player: wavelink.Player, track: wavelink.Track, reason):
    ctx = player.ctx
    vc: player = ctx.voice_client
    if vc.loop:
        return await vc.play(track)
    try:
        next_song = vc.queue.get()
        await vc.play(next_song)
        embed = discord.Embed(
            title="Now playing", description=f'Song name: **{next_song.title}**\nSong author: **{next_song.author}**')
        await ctx.send(embed=embed)
    except:
        # An exception when after the track end, the queue is now empty. If you dont do this, it will get error.
        await vc.stop()
@bot.command()
async def play(ctx: commands.Context, *, search: wavelink.YouTubeTrack):
    if not ctx.voice_client:
        vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
    elif not getattr(ctx.author.voice, 'channel', None):
        await ctx.send(f'Connect to a voice channel to use this command!')
    else:
        vc: wavelink.Player = ctx.voice_client
    song_name = search.title
    song_author = search.author
    if song_author == None:
        song_author = 'Unknown'
    # embed = discord.Embed(title="Added to queue", description=f'Song name: **{song_name}**\nSong author: **{song_author}**')
    # await vc.play(search)
    # await ctx.send(embed=embed)
    if vc.queue.is_empty and vc.is_playing:
        await vc.play(search)
        embed = discord.Embed(title="Playing", description=f'Song name: **{song_name}**\nSong author: **{song_author}**')
        return await ctx.send(embed=embed)
    else:
        await vc.queue.put_wait(search)
        embed = discord.Embed(title="Added to queue", description=f'Song name: **{song_name}**\nSong author: **{song_author}**')
        return await ctx.send(embed=embed)
    vc.ctx = ctx
    setattr(vc, "loop", False)
@bot.command()
async def pause(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send('Im not playing any music!')
    elif not getattr(ctx.author.voice, 'channel', None):
        await ctx.send(f'Connect to a voice channel to use this command!')
    else:
        vc: wavelink.Player = ctx.voice_client
    await vc.pause()
    await ctx.send(f'Paused!')

@bot.command()
async def resume(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send('Im not playing any music!')
    elif not getattr(ctx.author.voice, 'channel', None):
        await ctx.send(f'Connect to a voice channel to use this command!')
    else:
        vc: wavelink.Player = ctx.voice_client
    await vc.resume()
    await ctx.send(f'Resumed!')

@bot.command()
async def stop(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send('Im not playing any music!')
    elif not getattr(ctx.author.voice, 'channel', None):
        await ctx.send(f'Connect to a voice channel to use this command!')
    else:
        vc: wavelink.Player = ctx.voice_client
    await vc.stop()
    await ctx.send(f'Stopped!')

@bot.command()
async def disconnect(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send('Im not playing any music!')
    elif not getattr(ctx.author.voice, 'channel', None):
        await ctx.send(f'Connect to a voice channel to use this command!')
    else:
        vc: wavelink.Player = ctx.voice_client
    await vc.disconnect()
    await ctx.send('Bye!')

@bot.command()
async def loop(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send('Im not playing any music!')
    elif not getattr(ctx.author.voice, 'channel', None):
        await ctx.send(f'Connect to a voice channel to use this command!')
    else:
        vc: wavelink.Player = ctx.voice_client
    try:
        vc.loop = True
    except Exception:
        setattr(vc, "loop", False)
    if vc.loop:
        return await ctx.send('Loop is now enabled!')
    else:
        vc.loop = False
        return await ctx.send('Loop is now disabled')

@bot.command()
async def queue(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send('Im not playing any music!')
    elif not getattr(ctx.author.voice, 'channel', None):
        await ctx.send(f'Connect to a voice channel to use this command!')
    else:
        vc: wavelink.Player = ctx.voice_client

    if vc.queue.is_empty:
        return await ctx.send('Queue is empty!')
    embed = discord.Embed(title="Queue")
    queue = vc.queue.copy()
    song_count = 0
    for song in queue:
        song_count += 1
        embed.add_field(name=f"Song number {song_count}", value=f"{song.title}")

    return await ctx.send(embed=embed)
bot.run('secret')