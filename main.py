import os
import discord
from discord.ext import commands

token = "NzU5ODA5Njk3NjY1OTA4NzU3.X3C57A.3eNlO8gdfuWBiE8aYFH1EN6GKlg"#os.environ["NzU5ODA5Njk3NjY1OTA4NzU3.X3C57A.3eNlO8gdfuWBiE8aYFH1EN6GKlg"]
bot = commands.Bot(command_prefix="!")


@bot.command(name="ping", help='Send ping pong message')
async def pong(ctx):
    await ctx.message.channel.send("Pong",)

bot.run(token, bot=True)