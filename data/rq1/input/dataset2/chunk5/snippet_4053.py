#Source: https://stackoverflow.com/questions/59437405/why-when-i-run-my-script-the-downloaded-image-files-have-zero-bytes-and-i-recei
import praw, requests, os, bs4

reddit = praw.Reddit(client_id='xxxx', 
                      client_secret='xxxx',
                      user_agent='picture downloader',
                      username='xxxx',
                      password='xxxx'
                      ) 
print(reddit.read_only)

os.makedirs('redditpics', exist_ok=True) 
for submission in reddit.subreddit('earthporn').hot(limit=50):
    url = submission.url
    print(url)
    imageFile = open(os.path.join('redditpics', os.path.basename(url)), 'wb')
print('Done')