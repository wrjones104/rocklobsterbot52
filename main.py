import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Client(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.run(os.getenv('DISCORD_TOKEN'))
