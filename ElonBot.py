import discord
import random
import asyncio
import pickle
import tracemalloc

from discord.utils import get
from discord.ext import commands, tasks
from collections import defaultdict
tracemalloc.start()

client = commands.Bot(command_prefix = '\\')
#teslas = []
#pickle.dump(teslas, open("teslas.dat", "wb"))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='PewDiePie', url = 'https://www.twitch.tv/pewdiepie/'))
    print('Start your engines.')

@client.event 
async def on_member_update(before, after): # Detects when a member updates profile
    if not before.nick == after.nick:
        channel = client.get_channel(599310168307662889)
        await channel.send(f'Nickname Changed:\n{before.name} --> {after.nick}') #logs nickname changes in bot-channel

##############
## Commands ##
##############

## Echo ##
@client.command()
@commands.has_any_role('Owners','Moderator', 'Admin')
async def echo(ctx, *, message): ## Repeats message given by user calling the command
    await ctx.channel.purge(limit = 1)
    await ctx.send(f'{message}')
    return

# Load coinamount from coinsamount.dat
@client.command()
async def coin(ctx, member : discord.Member):
    coinamount = pickle.load(open("D:\\source\\repos\\RussianHackBot\\RussianHackBot\\RussianHackBot\\balance.dat", "rb")) # Load dictionary of members' coin balances
    await ctx.send(f'{coinamount.get(member.name)}')

client.run('NjA4NDAxNjI4NzU5ODUxMDg1.XUnorg.P294z_bOakijal57hOTPC2Hyfac')