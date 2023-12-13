import os
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from datetime import datetime, timedelta

# wrapper / decorator
message_lastseen = datetime.now()
message2_lastseen = datetime.now()

bot = commands.Bot(command_prefix='k!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def test(ctx, *, par):
    await ctx.channel.send(f"You typed {par}")

@bot.command()
async def custom_help(ctx):
    # Your custom help command logic here
    em_bed = discord.Embed(title="Shenhe Bot help", description="All available bot commands", color=0x117fed)
    em_bed.add_field(name="help", value="Get help command", inline=False)
    em_bed.add_field(name="test", value="Respond message that you've sent", inline=False)
    em_bed.add_field(name="send", value="Send hello message to user", inline=False)
    em_bed.add_field(name="play", value="Listen to music", inline=False)
    em_bed.set_thumbnail(url='https://i.pinimg.com/564x/57/95/03/579503ddd342c1a1891fac0b46434f77.jpg')
    em_bed.set_footer(text='Shenhe', icon_url='https://i.pinimg.com/564x/57/95/03/579503ddd342c1a1891fac0b46434f77.jpg')
    await ctx.channel.send(embed=em_bed)

@bot.command()
async def send(ctx):
    print(ctx.channel)
    await ctx.channel.send('Hello')

# ... (rest of your code)

bot.run(os.environ['TOKEN'])
