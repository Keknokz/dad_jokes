import discord 
from discord.ui import Button, View
from discord.ext import commands
# this is just the import 

from joke_picker import rand_joke

f1 = 'jokes/start_up.txt'
f2 = 'jokes/punch_line.txt'
# these are the files in which the jokes are held

intents = discord.Intents.default()
intents.message_content = True
# i have no clue what this does

TOKEN = 'OTg2MzM1MzMzOTI0ODc2MzQ4.GLpJkC.K7_cuh5A3nwVf7_nDZdL50MBd-tZZtji6ORt5c'
# this is the token i use to use the api

client = discord.Client(intents=intents)
# this is the client 

@client.event # and event is when anything happens
async def on_ready(): # async just means it waits for stuff to happen
    print(f"We have logged in successfully as {client.user}") # this shows us if we logged in successfully
    
@client.event 
async def on_message(message): # this waits for a message to be sent in the channel
    start_joke, end_joke = rand_joke(f1, f2)
    # this gets randoms jokes
   
    button = Button(label=start_joke, style=discord.ButtonStyle.green) 
    view = View() # need this to make the button show
    view.add_item(button)
    # this is all to make the button
    
    async def button_callback(interaction):
        await interaction.response.edit_message(content=end_joke, view=None)
        # this is just what happens when the button is pressed
        
    button.callback = button_callback
            
    if message.author == client.user: # this checks if the message came from the bot
        return # this makes it do nothing
    
    if message.channel.name == 'general': # this checks if the channel is general
        if message.content.startswith("!joke"): # this checks if the message they just sent has the keywords in them
            await message.channel.send(view=view) # this makes the button appear
        
client.run(TOKEN) # this just runs it