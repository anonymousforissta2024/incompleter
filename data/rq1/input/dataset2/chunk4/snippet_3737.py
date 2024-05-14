#Source: https://stackoverflow.com/questions/36129435/type-error-unhashable-type-list-in-praw-bot
#Bot

import praw
import time
import re
import os

r = praw.Reddit(user_agent = "Bot")
r.login()
cache = []



def run_bot():
    subreddit = r.get_subreddit("broap")
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        comment_text = comment.body.lower()
        author = comment.author
        url = comment.link_id
        msg = "User {} has tagged you in a post!".format(author)
        words = filter( lambda x:x.startswith('//'), comment_text.split())
        user = words[2:]  
        if comment.id not in cache and words:
            r.user.send_message(user ,msg)
            cache.add(comment.id)




while True:
    run_bot()
    time.sleep(5)