#Source: https://stackoverflow.com/questions/61782444/using-praw-to-scrape-a-list-of-subreddits-typeerror-subreddit-object-is-not
subs= ["sub1","sub2", "sub3", "sub4"]

commentsDict = {"comment_user": [], "comment_text":[], "comment_score":[], "comment_date":[] }
postsDict = {"post_title" : [], "post_score" : [], "post_comments_num":[], "post_date":[], \
                "post_user":[], "post_text":[], "post_id":[]}

for i in range(len(subs)):
    for submission in reddit.subreddit(subs[i]):
        submission.comment_sort = 'new'
        comments = list(submission.comments)
        for comments in submission.comments:
            postsDict["post_title"].append(submission.title)#title of post with comment
            postsDict["post_score"].append(submission.score)#upvotes-downvotes
            postsDict["post_text"].append(submission.selftext)#get body of post
            postsDict["post_id"].append(submission.id)#unique id address for post
            postsDict["post_user"].append(submission.author)  #user name of poster
            postsDict["post_comments_num"].append(submission.num_comments) #number of comments on post
            date = submission.created_utc                                  #create variable for date
            timestamp = datetime.datetime.fromtimestamp(date)              #create variable to translate unix date 
            postsDict["post_date"].append(timestamp.strftime('%Y-%m-%D %H:%M:%S')) #extract date and add to dict
            for top_level_comment in submission.comments:                   #create loop for extracting comments
                if isinstance(top_level_comment, MoreComments):
                    continue
            submission.comments.replace_more(limit=None)                   #tell Praw to click more comments and get those too
            commentsDict["comment_user"].append(comments.author)              #get comment username
            commentsDict["comment_score"].append(comments.score)            #comment upvotes-downvotes
            date = comments.created                                         #same date as above but for comments
            timestamp = datetime.datetime.fromtimestamp(date)
            commentsDict["comment_date"].append(timestamp.strftime('%Y-%m-%D %H:%M:%S')) #add translated unix date to dict
            commentsDict["comment_text"].append(comments.body)      #get comment text 