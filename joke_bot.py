import discord 
from discord.ui import Button, View
from discord.ext import commands
from do_not_show import TOKEN
# this is just the import 

from joke_picker import rand_joke
# this imports the function to get a random joke


intents = discord.Intents.default()
intents.message_content = True
# i have no clue what this does

client = discord.Client(intents=intents)
# this is the client 

@client.event # and event is when anything happens
async def on_ready(): # async just means it waits for stuff to happen
    print(f"We have logged in successfully as {client.user}") # this shows us if we logged in successfully
    
@client.event 
async def on_message(message): # this waits for a message to be sent in the channel
    start_joke, end_joke = rand_joke()
    # this gets random jokes
   
    button = Button(label=start_joke, style=discord.ButtonStyle.green) 
    view = View() # need this to make the button show
    view.add_item(button)
    # this is all to make the button 
    # and to chose the style of the button
    
    async def button_callback(interaction):
        await interaction.response.edit_message(content=end_joke, view=None)
        # when the button is pressed it sends the body of the joke
        # and takes away the button
        
    button.callback = button_callback
            
    if message.author == client.user: # this checks if the message came from the bot
        return # this makes it do nothing
    
    if message.channel.name == 'general': # this checks if the channel is general
        if message.content.startswith("!joke"): # this checks if the message they just sent has the keywords in them
            await message.channel.send(view=view) # this makes the button appear
        
client.run(TOKEN) # this just runs it