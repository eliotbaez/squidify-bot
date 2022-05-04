#!/usr/bin/python3

import discord
from discord.ext import commands
import squidify
import private
import re
import sys


# the code goes here
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print ("SquidifyBot is now online!")
    print("Active in the follwing servers:")
    for guild in client.guilds:
        print("\t" + guild.name)
        

@client.event
async def on_message(message):
    if message.author != client.user:
        # no recursion please
        if message.channel.name == "squ":
            # we are now clear to do stuff
            await message.channel.send(content=squidify.squidify_string(message.content))
            # we should add some logging here, but later


@client.command(name = "syn")
async def h_function(ctx, * arg):
    await ctx.send("ack")


if __name__ == "__main__":
    client.run(private.token)
