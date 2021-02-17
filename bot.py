# bot.py
import os

import discord
from dotenv import load_dotenv

import startup
import strings
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

startup.loadData()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

def handleMessage(message):
    clean = message[1:]

    if '8ball' in clean:
        eList = startup.eight_ball_resps
        return random.choice(eList)
    elif 'nlb' in clean:
        return "Fuck you Lloyd, the NLB isn't in D2.\n" \
           "Just play with the Dead Man's Tale you whiny bitch."
    elif 'command' in clean:
        return strings.cmds
    else:
        return 'Check out this fuckin jokester trying to command me to do something that I don\'t wanna do. \n' \
               'Type **!commands** for a list of the available commands'

@client.event
async def on_message(message):
    lower = message.content.lower()
    noSpace = lower.strip(' ')  # remove whitespaces

    if '!' == noSpace[0]:
        await message.channel.send(handleMessage(noSpace))

client.run(TOKEN)