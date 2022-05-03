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


@client.command(name = "syn")
async def h_function(ctx, * arg):
    await ctx.send("ack")


if __name__ == "__main__":
    client.run(private.token)
