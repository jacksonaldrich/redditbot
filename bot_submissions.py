import praw
import random
import time

reddit = praw.Reddit('bot')

list_of_submissions = list((reddit.subreddit("liberal").hot(limit=10000)))
# Takes the list of the hot submissions from the r/liberal subreddit
# Altough I could make the limit=None, that would most likely take a very long time, so I limited it to a smaller number
# I chose from the "hot" in the subreddit, since those would most likely be better / more liked posts

subreddit = reddit.subreddit('cs40_2022fall')
for i in range (500): # limited the loop to 500, but we only need 200 submissions
    submission = random.choice(list_of_submissions)
    content = submission.selftext
    title = submission.title
    if content == '': # if the string is empty, then it'll have a URL. If not, then there is no URL
        link = submission.url
        subreddit.submit(title, url = link)
        print(title)
    else:
        subreddit.submit(title, selftext = content)
        print(title)
    time.sleep(5)