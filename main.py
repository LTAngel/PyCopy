#import discord
import discord
import json
import asyncio
from discord.ext import commands

client = discord.Client()

with open('config.json') as f:
    config = json.load(f)

Token = config.get('Token')
originChannel = config.get('originChannel')
sendChannel = config.get('sendChannel')
authorID = config.get('authorID')


async def see_mvpChan(ctx):
    return ctx.channel.id == originChannel


@client.event
async def on_ready():
    print("ready")

@client.event
@commands.check(see_mvpChan)
async def on_message(message):

    sendChan = client.get_channel(sendChannel)

    print("saw message")
    

    if message.author == client.user:
        print("message from myself")
        return

    elif message.author.id == authorID:

        
        print("trying to send, found right channel and right person and right title")

        resendEmb = message.embeds[0]
        await sendChan.send(embed = resendEmb)

        return
    








client.run(Token, bot = False)


