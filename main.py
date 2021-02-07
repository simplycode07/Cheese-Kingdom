import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = ".")

client.remove_command("help")
token = os.environ.get('TECH_AND_GAMING_BOT')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload(f'cogs.{extension}')
    
for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")
        
client.run(token)
