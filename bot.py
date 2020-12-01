#You Need To pip install discord
TOKEN = "Your Token Here"

import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('bot is ready')
    
#BOT COMMAND GO HERE


client.run(TOKEN)
