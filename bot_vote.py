import praw
from textblob import TextBlob

# These are the keywords that the bot looks for
goodwords = ['biden', 'obama', 'hillary']
badwords = ['trump']

# If the good keywords are contained in the post or comment, the bot will upvote
# If the bad keywords are contained in the post or comment, the bot will downvote
def vote(submission):
    submission.comments.replace_more(limit=None)
    normalized_title = submission.title.lower()
    normalized_comments = submission.comments.list()
    for phrase in goodwords:
        if phrase in normalized_title:
            textblob=TextBlob(submission.title)
            polarity=textblob.sentiment.polarity
            print('polarity=',polarity)
            if polarity>=0.0:
                submission.upvote()
                print('Submission Upvoted') 
                break
            else:
                submission.downvote()
                print('Submission Downvoted')
                break 

    for comment in normalized_comments:
        lowercase = comment.body.lower()
        for phrase in goodwords:
            if phrase in lowercase:
                textblob=TextBlob(comment.body)
                polarity=textblob.sentiment.polarity
                print('polarity=',polarity)
                if polarity>=0.0:
                    comment.upvote()
                    print('Comment Upvoted') 
                    break
                else:
                    comment.downvote()
                    print('Comment Downvoted')
                    break 

# Code below is for the "badwords"
    for phrase in badwords:
        if phrase in normalized_title:
            textblob=TextBlob(submission.title)
            polarity=textblob.sentiment.polarity
            print('polarity=',polarity)
            if polarity<=0.0:
                submission.upvote()
                # upvoting a submission with a negative sentiment of Trump
                # because this is actually supporting the overall preferences of the bot!
                print('Submission Upvoted') 
                break
            else:
                submission.downvote()
                print('Submission Downvoted')
                break  

    for comment in normalized_comments:
        lowercase = comment.body.lower()
        for phrase in badwords:
            if phrase in lowercase:
                textblob=TextBlob(comment.body)
                polarity=textblob.sentiment.polarity
                print('polarity=',polarity)
                if polarity<=0.0:
                    comment.upvote()
                    # upvoting a comment with a negative sentiment of Trump
                    # because this is actually supporting the overall preferences of the bot!
                    print('Comment Upvoted') 
                    break
                else:
                    comment.downvote()
                    print('Comment Downvoted')
                    break 

reddit = praw.Reddit('bot')

subreddit = reddit.subreddit('cs40_2022fall')
while True:
    for submission in list((reddit.subreddit("cs40_2022fall").hot(limit=None))):
        vote(submission)