import os
import discord
from discord.ext import commands

token = os.environ["DISCORD_TOKEN"]
bot = commands.Bot(command_prefix="!")


@bot.command(name="ping", help='Send ping pong message')
async def pong(ctx):
    await ctx.message.channel.send("Pong",)

bot.run(token, bot=True)