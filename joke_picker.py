import random

def read_jokes(file1, file2):
    # all this does is take the jokes and punch lines 
    # then put them in a dict
    
    try:
        with open(file1, 'r') as f:
            with open(file2, 'r') as f2:
                
                
                sta_joke = f.readlines()
                end_joke = f2.readlines()
                                                
                return sta_joke, end_joke
            
    except FileNotFoundError:
        print("jokes are not in the folder")
           
def rand_joke(f1, f2):
    # this is the function that will pick a random joke
    start_up, punch_line = read_jokes(f1, f2)

    num_jokes = 0
    
    for x in start_up:
        num_jokes += 1
    num_jokes -= 1
            
    rand_index = random.randint(0, num_jokes)
    
    joke_start = start_up[rand_index]
    joke_end = punch_line[rand_index]
    
    return joke_start, joke_end