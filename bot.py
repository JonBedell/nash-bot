import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

ROLL_DICE = '!roll'
WHY_AM_I_LOSING = 'WhyAmILosing!'

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    excuses = [
        '@Nacdaddy left a hole in his wall',
        '@the_crafts let raiders into your base',
        '@andrewkaye got Teutons again',
    ]

    if message.content == WHY_AM_I_LOSING:
        response = random.choice(excuses)
        await message.channel.send(response)
    elif message.content.startsWith(ROLL_DICE):
        response = roll_dice(message.content[len(ROLL_DICE):])
        await message.channel.send(response)

def roll_dice(num_sides = None):
    try:
        num_sides = int(num_sides)
    except:
        num_sides = 6
    return random.randrange(num_sides)+1

client.run(TOKEN)
