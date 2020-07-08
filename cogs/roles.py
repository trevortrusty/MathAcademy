
import discord
import random
import asyncio
from discord.utils import get
from discord.ext import commands, tasks
from datetime import datetime, timedelta
#from automessage import automessage

class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_any_role('Owners', 'Admin')
    async def role_react(self, ctx, MESSAGE_ID):
        myMessage = await ctx.fetch_message(MESSAGE_ID)
        await myMessage.add_reaction('1️⃣')
        await myMessage.add_reaction('2️⃣')
        await myMessage.add_reaction('3️⃣')
        await myMessage.add_reaction('4️⃣')
        await myMessage.add_reaction('5️⃣')
        await myMessage.add_reaction('6️⃣')
        await myMessage.add_reaction('7️⃣') #8️⃣9️⃣🔟0️⃣👍➕💡🤓🖥👨‍🎓
        await myMessage.add_reaction('8️⃣')
        await myMessage.add_reaction('9️⃣')
        await myMessage.add_reaction('🔟')
        await myMessage.add_reaction('0️⃣')
        await myMessage.add_reaction('👍')
        await myMessage.add_reaction('➕')
        await myMessage.add_reaction('💡')
        await myMessage.add_reaction('🤓')
        await myMessage.add_reaction('🖥')
        await myMessage.add_reaction('👨‍🎓')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        #print(f'{user} has added a reaction')    
        #m = self.client.fetch_message(608054063346745376)
        #m  = discord.abc.Messageable.fetch_message(608054063346745376)
        #m = await self.client.get_message(self.client.get_channel(608045584921919489), 608054063346745376)
        #member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        async def addRole(roleName):
            currentRole = discord.utils.get(payload.member.guild.roles, name = roleName)
            await payload.member.add_roles(currentRole)
            if payload.member.dm_channel is None:
                await payload.member.create_dm()
            await payload.member.dm_channel.send(f'Added {roleName}')

        if payload.message_id == 725555221194997790:
            if payload.emoji.name == '1️⃣':
                await addRole("Algebra")
            elif payload.emoji.name == '2️⃣':
                await addRole("Geometry")
            elif payload.emoji.name == '3️⃣':
                await addRole("Trigonometry")
            elif payload.emoji.name == '4️⃣':
                await addRole("Pre-calculus")
            elif payload.emoji.name == '5️⃣':
                await addRole("Calculus 1")
            elif payload.emoji.name == '6️⃣':
                await addRole("Calculus 2")
            elif payload.emoji.name == '7️⃣':
                await addRole("Calculus 3")
            elif payload.emoji.name == '8️⃣':
                await addRole("Linear Algebra")
            elif payload.emoji.name == '9️⃣':
                await addRole("Differential Equations")
            elif payload.emoji.name == '🔟':
                await addRole("Statistics")
            elif payload.emoji.name == '0️⃣':
                await addRole("Discrete Math")
            elif payload.emoji.name == '👍':
                await addRole("Physics")
            elif payload.emoji.name == '➕':
                await addRole("Mathematics")
            elif payload.emoji.name == '💡':
                await addRole("Engineering")
            elif payload.emoji.name == '🤓':
                await addRole("Nerd")
            elif payload.emoji.name == '🖥':
                await addRole("Computer Science")
            elif payload.emoji.name == '👨‍🎓':
                await addRole("Student")
    
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        async def removeRole(roleName):
            myGuild = self.client.get_guild(payload.guild_id)
            myMember = myGuild.get_member(payload.user_id)
            currentRole = discord.utils.get(myMember.guild.roles, name = roleName)
            await myMember.remove_roles(currentRole)
            if myMember.dm_channel is None:
                await myMember.create_dm()
            await myMember.dm_channel.send(f'Removed {roleName}')

        if payload.message_id == 725555221194997790:
            if payload.emoji.name == '1️⃣':
                await removeRole("Algebra")
            elif payload.emoji.name == '2️⃣':
                await removeRole("Geometry")
            elif payload.emoji.name == '3️⃣':
                await removeRole("Trigonometry")
            elif payload.emoji.name == '4️⃣':
                await removeRole("Pre-calculus")
            elif payload.emoji.name == '5️⃣':
                await removeRole("Calculus 1")
            elif payload.emoji.name == '6️⃣':
                await removeRole("Calculus 2")
            elif payload.emoji.name == '7️⃣':
                await removeRole("Calculus 3")
            elif payload.emoji.name == '8️⃣':
                await removeRole("Linear Algebra")
            elif payload.emoji.name == '9️⃣':
                await removeRole("Differential Equations")
            elif payload.emoji.name == '🔟':
                await removeRole("Statistics")
            elif payload.emoji.name == '0️⃣':
                await removeRole("Discrete Math")
            elif payload.emoji.name == '👍':
                await removeRole("Physics")
            elif payload.emoji.name == '➕':
                await removeRole("Mathematics")
            elif payload.emoji.name == '💡':
                await removeRole("Engineering")
            elif payload.emoji.name == '🤓':
                await removeRole("Nerd")
            elif payload.emoji.name == '🖥':
                await removeRole("Computer Science")
            elif payload.emoji.name == '👨‍🎓':
                await removeRole("Student")

        
    #@commands.Cog.listener()
    #async def on_raw_reaction_add(self, payload):
    #    # Computer Science guild CS role reactions
    #    if payload.message_id == 640010728597880850:
    #        print(payload.emoji.name)
    #        # Find a role corresponding to the Emoji name.
    #        guild_id = payload.guild_id
    #        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

    #        role = discord.utils.find(lambda r : r.name == payload.emoji.name, guild.roles)

    #        if role is not None:
    #            print(role.name + " was found!")
    #            print(role.id)
    #            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
    #            await member.add_roles(role)
    #            print("done")
    #    # Math server COLOR role reactions
    #    elif payload.message_id == 660302314707484682:
    #        print(payload.emoji.name)
    #        # Find a role corresponding to the Emoji name.
    #        guild_id = payload.guild_id
    #        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

    #        role = discord.utils.find(lambda r : r.name == payload.emoji.name, guild.roles)

    #        if role is not None:
    #            print(role.name + " was found!")
    #            print(role.id)
    #            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
    #            await member.add_roles(role)
    #            print("done")  


def setup(client):
    client.add_cog(Roles(client))

