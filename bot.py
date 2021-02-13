# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

def handleMessage(message):
    return "Fuck you Lloyd, the NLB isn't in D2."

def mCheck(message):
    clean = message[1:]
    return 'nlb' in clean.lower()

@client.event
async def on_message(message):
    lower = message.content.lower()
    noSpace = lower.strip(' ')  # remove whitespaces

    if '!' == noSpace[0] and mCheck(noSpace):
        await message.channel.send(handleMessage(noSpace))

client.run(TOKEN)