import random

from joke_finder import get_joke
# this is the function that gets the jokes from reddit
        
def rand_joke():
    # this is the function that will pick a random joke
    
    jokes = get_joke()
    
    num_jokes = len(jokes.keys())
    num_jokes - 1
    # this is how many jokes are in the list
    
    joke_titles = list(jokes.keys()) 
    # this makes it so its not saved as a dict object
    joke_bodys = []
    
    for x in jokes.keys():
        joke_bodys.append(jokes[x])
    
    rand_index = random.randint(0, num_jokes)
    # this pick a random number
    
    joke_leadup = joke_titles[rand_index]
    joke_punch = joke_bodys[rand_index]
    # this picks a random joke from the lists and returns them
      
    return joke_leadup, joke_punch 