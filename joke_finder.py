import praw

from do_not_show import client_id, client_secret, user, passw
# this is passwords and importent stuff

reddit = praw.Reddit(
	client_id = client_id,
	client_secret = client_secret,
	password = passw,
 	user_agent = 'Python joke_bot for discord by u/keknokzz',
	username = user
)

def get_joke():
    # this gets jokes from reddit
    
    jokes = {}
    
    for submission in reddit.subreddit('dadjokes').hot(limit=10):
        joke_title = submission.title
        joke_body = submission.selftext
        
        jokes[joke_title] = joke_body
        
    return jokes
