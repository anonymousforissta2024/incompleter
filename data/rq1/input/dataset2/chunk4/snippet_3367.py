#Source: https://stackoverflow.com/questions/66663801/errorhandling-indexerror-and-attribute-error-with-discordpy
@bot.command()
async def redditsearch(ctx, sub):
    start_time = time.time()
    listing = []
    subreddit = await reddit.subreddit(sub)
    print(subreddit.subreddit_type)
    if sub.lower() in bannedsubs:
        await ctx.send("Banned subreddit.")
        return
    elif subreddit.over18 == True:
        await ctx.send("No NSFW subreddits.")
        return
    else:
        async for submission in subreddit.hot(limit=100):
            if submission.url.endswith(("jpg", "jpeg", "png", "gifv")) and not submission.spoiler and not submission.over_18:
                listing.append(submission)
            else:
                pass
    
        random.shuffle(listing)
        post = listing[0]
        if submission.link_flair_text == None:
            await ctx.send(f"{post.title}\n{post.url}")
        else:
            await ctx.send(f"[{submission.link_flair_text}] \n{post.title}\n{post.url}")
        end_time = time.time()
        await ctx.send(f"---- Took %s seconds to lookup ----" % (end_time - start_time))