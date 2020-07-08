#!/usr/bin/python3

import discord
import os
from discord.ext import commands, tasks
from paths import file, cogs_path
from thetoken import the_token

client = commands.Bot(command_prefix = '\\')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.purge(limit = 1)
    
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.channel.purge(limit = 1)

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.purge(limit = 1)

for filename in os.listdir(cogs_path):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[: -3]}')

client.run(the_token)
