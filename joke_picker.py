import random

from joke_fi import get_joke
# this is the function that gets the jokes from reddit
        
def rand_joke():
    # this is the function that will pick a random joke
    
    jokes = get_joke()
    # this uses the function i made to get the jokes from reddit
    
    joke_titles = list(jokes.keys()) 
    # this makes it so its not saved as a dict object
    joke_bodys = []
    
    for x in jokes.keys():
        joke_bodys.append(jokes[x])
        # this adds the jokes punch line to the right list
        
    rand_index = random.randint(0, len(joke_titles))
    # this pick a random number
    
    try:
        joke_leadup = joke_titles[rand_index]
        joke_punch = joke_bodys[rand_index]
    except IndexError:
        rand_index = random.randint(0, len(joke_titles))
        joke_leadup = joke_titles[rand_index]
        joke_punch = joke_bodys[rand_index]
    # this trys to pick a random joke
    # but if it gets an error it just trys to pick a different one
      
    return joke_leadup, joke_punch
    