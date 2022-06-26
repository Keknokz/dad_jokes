import praw

reddit = praw.Reddit(
	client_id = 'FBQfYpYglDrK8l2ggHFvWQ',
	client_secret = '6ilZkWINWXXXYxNr8QDYsGEZy4IDtg',
	password = 'Googolplex07',
 	user_agent = 'Python joke_bot for discord by u/keknokzz',
	username = 'keknokzz'
)

subreddit = reddit.subreddit('dadjokes')

for submission in reddit.subreddit('dadjokes').hot(limit=2):
    print(submission.title)
    print(submission.selftext)
    print('\n')