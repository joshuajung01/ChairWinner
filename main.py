import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.environ["DISCORD_TOKEN"]
bot = commands.Bot(command_prefix="!")

# !search <site> <query>
# 
# !search amazon "pencil"
# !search ebay "pencil"
# !search all "pencil" (ideal?)

from amazon_search import amazon_search

sites = {
    "amazon": amazon_search
}

@bot.command()
async def search(ctx, site, query):
    await sites[site](ctx, query)

bot.run(token, bot=True)