#Source: https://stackoverflow.com/questions/64941040/extension-cogs-reddit-raised-an-error-typeerror-init-missing-1-require
import discord, praw, random
from discord.ext import commands

reddit = praw.Reddit(client_id = '<id>', client_secret = '<secret>', username = '<username>', password = '<password>', user_agent = 'pythonpraw') # this is undoubtedly all correct


# There is an underscore in this class identifier because a "Reddit" class already exists within the "praw" package
class _Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def meme(self, ctx):
        subreddit = reddit.subreddit('memes')
        top = subreddit.top(limit=50)
        all_submissions = []

        for submission in top:
            all_submissions.append(submission)

        random_submission = random.choice(all_submissions)

        submission_name = random_submission.title
        submission_url = random_submission.url

        embed = discord.Embed(title=submission_name)
        embed.set_image(url=submission_url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(_Reddit())