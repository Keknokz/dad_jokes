# https://github.com/Keknokz

# for discord functionality
import discord
# for loading cogs
import os

# for discord slash commands
from discord.ext import commands

from do_not_show import TOKEN


# for waiting for reddit api
import asyncio

class DadJokes(commands.Bot):
    
    def __init__(self) -> None:
        super().__init__(
            command_prefix = "!",
            intents = discord.Intents.all()
        )
        
    async def on_ready(self):
        
        print("Connected")
        
        synced = self.tree.sync()
        
    async def setup_hook(self) -> None:
        
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"cogs.{file[:-3]}")
        
bot = DadJokes()

bot.run(TOKEN)







# async def main() -> None:
    
#     test = JokeFinder()
    
#     task = asyncio.create_task(test.getJoke())
    
#     print("Getting jokes")
#     jk = await task
#     print("Here are jokes")
    
#     for i in jk:
#         print("!")
        
# asyncio.run(main())

# # for waiting for reddit api
# import asyncio