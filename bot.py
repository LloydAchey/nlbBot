# bot.py
import os

import discord
from dotenv import dotenv_values

import startup
import strings
import random

temp = dotenv_values(".env")
TOKEN = temp['DISCORD_TOKEN']

client = discord.Client()

startup.loadData()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

def handleMessage(text, message):
    clean = text[1:]

    if '8ball' in clean:
        eList = startup.eight_ball_resps
        return message.author.display_name + "  --  " + random.choice(eList)
    elif 'nlb' in clean:
        return "Fuck you Lloyd, the NLB isn't in D2.\n" \
           "Just play with the Dead Man's Tale you whiny bitch."
    elif 'command' in clean:
        return strings.cmds
    elif 'fuck' in clean:
        return 'HEY ' + message.author.display_name.upper() + '!  \n\n' \
                'Stop being a potty mouth.  Watch it buster.'
    else:
        return 'Check out ' + message.author.display_name + ' being a fuckin jokester, ' \
                    'trying to make me to do something that I don\'t wanna do. \n' \
                    'Type **!commands** for a list of the available commands'

@client.event
async def on_message(message):
    lower = message.content.lower()
    noSpace = lower.strip(' ')  # remove whitespaces

    if len(noSpace) > 0 and ('!' == noSpace[0] or '!8ball' in noSpace):
        await message.channel.send(handleMessage(noSpace, message))

client.run(TOKEN)