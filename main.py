import os
import pytz
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from keep_alive import keep_alive
from datetime import datetime

bot = commands.Bot(command_prefix='k!', intents=discord.Intents.all())

load_dotenv()
TOKEN = os.environ.get('TOKEN')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

@bot.event
async def on_voice_state_update(member, before, after):
    notification_channel = bot.get_channel(1134149073662922753)
    thai_timezone = pytz.timezone('Asia/Bangkok')
    timestamp_utc = datetime.utcnow()
    timestamp_thai = timestamp_utc.replace(tzinfo=pytz.utc).astimezone(thai_timezone)
    formatted_timestamp = timestamp_thai.strftime("%A at %I:%M %p")

    if notification_channel is None:
        return

    if before.channel != after.channel:
        # Member joined or left a voice channel
        if after.channel is not None:
            join = discord.Embed(
                title='Joined',
                description=f'{member} has joined {after.channel.name}.',
                color=0x3559E0,
            )
            join.set_footer(text=formatted_timestamp)
            await notification_channel.send(embed=join)
        elif before.channel is not None:
            left = discord.Embed(
                title='Left',
                description=f'{member} has left {before.channel.name}.',
                color=0x3559E0,
            )
            left.set_footer(text=formatted_timestamp)
            await notification_channel.send(embed=left)

@bot.event
async def on_message(message):
    mes = message.content
    if mes == 'hello':
        await message.channel.send("Hello It's me!")

    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")

@bot.tree.command(name='hellobot', description='Replies with Hello')
async def hellocommand(interaction):
    await interaction.response.send_message(f"Hello {interaction.user.name}!")

@bot.tree.command(name='help', description='help command')
async def helpcommand(interaction):
    helpembed = discord.Embed(
        title='Help',
        description='Bot Commands',
        color=0x3559E0,
        timestamp=discord.utils.utcnow()
    )
    await interaction.response.send_message(embed=helpembed)

keep_alive()

bot.run(TOKEN)