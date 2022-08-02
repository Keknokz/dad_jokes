import praw

from do_not_show import user, passw

reddit = praw.Reddit(
	client_id = 'FBQfYpYglDrK8l2ggHFvWQ',
	client_secret = '6ilZkWINWXXXYxNr8QDYsGEZy4IDtg',
	password = passw,
 	user_agent = 'Python joke_bot for discord by u/keknokzz',
	username = user
)

jokes = {}

for submission in reddit.subreddit('dadjokes').hot(limit=10):
    joke_title = submission.title
    joke_body = submission.selftext
    
    jokes[joke_title] = joke_body 
