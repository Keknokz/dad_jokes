# https://github.com/Keknokz

# for reddit api
import praw
# for waiting on the reddit API
import asyncio

# for my client id and secret as well as my reddit login
from do_not_show import client_id, client_secret, user, passw

class JokeFinder:
    
    def __init__(self):
        
        # makes a praw instance with correct details
        self.reddit = praw.Reddit(
            client_id = client_id,
            client_secret = client_secret,
            username = user,
            password = passw,
            user_agent = "Python dad joke bot for discord by u/keknokzz",
        )
    
    async def getJoke(self) -> list:
        
        jokes = {}
        
        for submission in self.reddit.subreddit('dadjokes').hot(limit=20):
            
            joke_title = submission.title
            joke_body = submission.selftext
            
            if len(joke_title) > 80:
                continue
            else:
                jokes[joke_title] = joke_body
                
        return jokes
    
    async def jokePicker(self, jokes) -> list:
        