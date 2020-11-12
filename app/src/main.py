# Import Discord Library 
import discord
import random, os
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv

BOT_PREFIX = ("?", "!")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client = Bot(command_prefix=BOT_PREFIX)
bot = commands.Bot(command_prefix='!')

# Setup Bot Client
client = discord.Client()

# 
@client.event
async def on_ready():
    print('Client has logged in as {0.user}'.format(client))

@bot.event
async def on_ready():
    print('Bot has logged in as {0.user}'.format(bot))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Meow, meow!')


@bot.command()
async def eight_ball(ctx):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    response = random.choice(possible_responses) + ", " + ctx.message.author.mention
    print(response)
    await ctx.send('what are you trying to say?' + response + " , " + ctx.message.author.mention)

@bot.command()
async def repeat(ctx, arg):
    await ctx.send(arg)

#client.run(TOKEN)

bot.run(TOKEN)