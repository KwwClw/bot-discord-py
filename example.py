import os
import discord

from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

from discord.ext import commands
from datetime import datetime, timedelta

# wrapper / decorator

message_lastseen = datetime.now()
message2_lastseen = datetime.now()

bot = commands.Bot(command_prefix='!',help_command=None)


@bot.event
async def on_ready():
    print(f"Logged in as (Client.user)")

@bot.command()
async def test(ctx, *,  par):
    await ctx.channel.send("You typed {0}".format(par))

@bot.command()
async def help(ctx):
    # help
    # test
    # send
    emBed = discord.Embed(title="Shenhe Bot help", description="All available bot commands", color=0x117fed)
    emBed.add_field(name="help", value="Get help command", inline=False)
    emBed.add_field(name="test", value="Respond message that you've send", inline=False)
    emBed.add_field(name="send", value="Send hello message to user", inline=False)
    emBed.add_field(name="play", value="Listen to muisic", inline=False)
    emBed.set_thumbnail(url='https://i.pinimg.com/564x/57/95/03/579503ddd342c1a1891fac0b46434f77.jpg')
    emBed.set_footer(text='Shenhe', icon_url='https://i.pinimg.com/564x/57/95/03/579503ddd342c1a1891fac0b46434f77.jpg')
    await ctx.channel.send(embed=emBed)

bot.command()
async def send(ctx):
        print(ctx.channel)
        await ctx.channel.send('Hello')

@bot.event # async/await
async def on_message(message):
    global message_lastseen, message2_lastseen
    if message.content == '!user':
        await message.channel.send(str(message.author.name) + ' Hello')
    elif message.content == 'เธอชื่ออะไร' and datetime.now() >= message_lastseen:
        message_lastseen =datetime.now() + timedelta(seconds=5)
        await message.channel.send('ฉันชื่อ' + str(bot.user.name))
        # logging
        print('{0} run นายชื่ออะไร at {1} and will be available again {2}'.format(message.author.name,datetime.now(),message_lastseen))
    elif message.content == 'ผมชื่ออะไร' and datetime.now() >= message2_lastseen:
        message2_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send('นายชื่อ ' + str(message.author.name)) 
    elif message.content == '!logout':
        await bot.logout()
    await bot.process_commands(message)

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_client == None:
        await ctx.channel.send("Joined")
        await channel.connect()
        voice_client = get(bot.voice_clients, guild=ctx.guild)

    YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not voice_client.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice_client.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice_client.is_playing()
    else :
        await ctx.channel.seed("Already playing song")
        return

@bot.command()
async def stop(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("bot is not connected to vc")
        return

    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send("this bot currently connected to {0}".format(voice_client.channel))
        return

    voice_client.stop()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()




bot.run(os.environ['TOKEN'])
