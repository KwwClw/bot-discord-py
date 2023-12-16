import os
import time
import pytz
import asyncio
import discord
import youtube_dl
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from keep_alive import keep_alive
from datetime import datetime

load_dotenv()
TOKEN = os.environ.get('TOKEN')

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='k!', intents=intents)

players = {}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    synced = await bot.tree.sync()
    if len(synced) <= 1:
        print(f"{len(synced)} command")
    else:
        print(f"{len(synced)} commands")

@bot.event
async def on_voice_state_update(member, before, after):
    notification_channel = bot.get_channel(1184790363337130074)
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
            # print(formatted_timestamp)
        elif before.channel is not None:
            left = discord.Embed(
                title='Left',
                description=f'{member} has left {before.channel.name}.',
                color=0x3559E0,
            )
            left.set_footer(text=formatted_timestamp)
            await notification_channel.send(embed=left)
            # print(formatted_timestamp)

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
    thai_timezone = pytz.timezone('Asia/Bangkok')
    timestamp_utc = datetime.utcnow()
    timestamp_thai = timestamp_utc.replace(tzinfo=pytz.utc).astimezone(thai_timezone)
    formatted_timestamp = timestamp_thai.strftime("%A at %I:%M %p")

    helpembed = discord.Embed(
        title='Help',
        description='Bot Commands',
        color=0x3559E0,
    )
    helpembed.set_footer(text=formatted_timestamp)
    await interaction.response.send_message(embed=helpembed)


@bot.tree.command(name='ping', description='Pong')
async def ping(interaction):
    start_time = time.time()

    # Simulate network latency with a sleep
    await asyncio.sleep(1)  # Adjust the duration as needed

    end_time = time.time()
    ping_duration = (end_time - start_time) * 1000

    api_ping = bot.latency * 1000  # Discord API ping in milliseconds

    pingembed = discord.Embed(
        title='📡 Connection',
        description=f'Ping is {api_ping:.2f} ms\nAPI Ping is {ping_duration:.2f} ms'
    )

    await interaction.response.send_message(content='🏓Pong!', embed=pingembed, ephemeral=True)

@bot.tree.command(name='play', description='Play your song')
async def play(ctx, url: str):
    if ctx.voice_client is None:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        players[ctx.guild.id] = vc
    else:
        vc = ctx.voice_client

    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']

    player = vc.play(discord.FFmpegPCMAudio(url2, **ffmpeg_options))
    players[ctx.guild.id] = player

keep_alive()

bot.run(TOKEN)