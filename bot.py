# bot.py
import os

import discord
from dotenv import dotenv_values

import startup
import strings
import random
import asyncio


temp = dotenv_values(".env")
TOKEN = temp['DISCORD_TOKEN']

client = discord.Client()

startup.loadData()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

async def joinVoice(channel):
    vc = await channel.connect()
    return vc

async def TylBehavior(message):
    #Need author to be in a voice channel and bot to not already be playing
    if message.author.voice is None:
        return "You must be in a voice channel."
    if message.guild.me.voice is not None:
        return "I'm already playing."

    channel = message.author.voice.channel
    line = random.choice(startup.tylVoiceLines)
    audio_source = discord.FFmpegPCMAudio(executable='C:/Users/Lloyd/node_modules/ffmpeg-static/ffmpeg.exe', source=line)

    vc = await joinVoice(channel)
    vc.play(audio_source)
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()


    return "Done Playing :)"

async def handleMessage(text, message):
    clean = text[1:]

    if '8ball' in clean:
        eList = startup.eight_ball_resps
        return message.author.display_name + "  --  " + random.choice(eList)
    elif 'nlb' in clean:
        return "Fuck you Lloyd, the NLB isn't in D2.\n" \
           "Just play with the Dead Man's Tale you whiny bitch."
    elif 'tyl' in clean or 'regor' in clean:
        return await TylBehavior(message)
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
        await message.channel.send(await handleMessage(noSpace, message))

client.run(TOKEN)