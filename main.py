import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables from .env
load_dotenv()

# Access the loaded environment variable
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("BOT ONLINE!")

bot.run(TOKEN)