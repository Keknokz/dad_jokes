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
# this is the reddit instance

def get_joke():
    # this gets jokes from reddit
    
    jokes = {}
    
    for submission in reddit.subreddit('dadjokes').hot(limit=20): 
        joke_title = submission.title
        joke_body = submission.selftext
        
        if len(joke_title) > 80:
            continue
        # this makes sure that the label isnt longer than 80 characters
        # if they are it just continues
        elif len(joke_title) <= 80:
            jokes[joke_title] = joke_body
            # this makes the dict to return with the jokes in it           
        
    return jokes
