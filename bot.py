import os
import converse

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='converse')
async def conversePrice(ctx):
    
    response = converse.getString()
    await ctx.send(response)


bot.run(TOKEN)