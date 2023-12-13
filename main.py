import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True

from keep_alive import keep_alive
keep_alive()

load_dotenv()

bot = commands.Bot(command_prefix='k!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_voice_state_update(member, before, after):
    notification_channel = bot.get_channel(1134149073662922753)

    if notification_channel is not None and before.channel != after.channel:
        if after.channel is not None:
            await notification_channel.send(f'{member.mention} has joined {after.channel.name}.')
        elif before.channel is not None:
            await notification_channel.send(f'{member.mention} has left {before.channel.name}.')

# @bot.event
# async def on_member_joined(member):
#     chanel = bot.get_channel(1134149073662922753)


bot.run(os.environ['TOKEN'])