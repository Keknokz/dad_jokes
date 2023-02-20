import discord 
from discord.ui import Button, View
from discord.ext import commands
# this is just the import 

from do_not_show import TOKEN

intents = discord.Intents.default()
intents.message_content = True
# i have no clue what this does

client = discord.Client(intents=intents)
# this is the client 
  
class MyView(View):
    
    @discord.ui.button(label="Jamie", style=discord.ButtonStyle.green) # this is just the button style and label
    async def button_callback(self, button, interaction):
        await interaction.response.edit_message(content="J ais mais boule ton t à gorge", view=None)
        # this waits for someone to click the button then edits the msg and removes the buttons

@client.event # and event is when anything happens
async def on_ready(): # async just means it waits for stuff to happen
    print(f"We have logged in successfully as {client.user}") # this shows us if we logged in successfully
    
@client.event 
async def on_message(message): # this waits for a message to be sent in the channel
    view = MyView() # need this to make the button show
    
    if message.author == client.user: # this checks if the message came from the bot
        return # this makes it do nothing
    
    if message.channel.name == 'general': # this checks if the channel is general
        if message.content.startswith("!joke"): # this checks if the message they just sent has the keywords in them
            await message.channel.send(view=view) # this makes the button appear
            #await message.channel.send("Deez nuts \nlmao gotem") # this waits to send a message if the if passes
        
client.run(TOKEN) # this just runs it