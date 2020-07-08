import discord
from discord.ext import commands, tasks

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def gethelp(self, ctx):
        role = discord.utils.get(ctx.message.guild.roles, name = 'WaitingForHelp')
        rChannel = self.client.get_channel(656296550443646986)
        await ctx.message.author.add_roles(role)
        await ctx.send('>>> Waiting for help')    
        await rChannel.send(f'>>> {ctx.message.author.mention} has requested help in {ctx.channel.mention}')

    @commands.command()
    async def endhelp(self, ctx, member : discord.Member = ''):
        waitRole = discord.utils.get(ctx.message.guild.roles, name = 'WaitingForHelp')
        helpRole = discord.utils.get(ctx.message.guild.roles, name = 'BeingHelped')
        
        if(member == ''):
            await ctx.message.author.remove_roles(waitRole)
            await ctx.message.author.remove_roles(helpRole)
        else:
            await member.remove_roles(waitRole)
            await member.remove_roles(helpRole)
        await ctx.send('>>> Help case closed!')
    
    @commands.command()
    async def starthelp(self, ctx, member : discord.Member):
        waitRole = discord.utils.get(ctx.message.guild.roles, name = 'WaitingForHelp')
        helpRole = discord.utils.get(ctx.message.guild.roles, name = 'BeingHelped')
        rChannel = self.client.get_channel(656296550443646986)
        await ctx.message.author.remove_roles(waitRole)
        await member.add_roles(helpRole)
        await ctx.send('>>> ✅') 
        await rChannel.send(f'>>> {ctx.message.author.mention} has accepted help request from {member.mention}')
        
    @commands.command()
    async def release(self, ctx):
        waitRole = discord.utils.get(ctx.message.guild.roles, name = 'WaitingForHelp')
        helpRole = discord.utils.get(ctx.message.guild.roles, name = 'BeingHelped')
        for member in ctx.guild.members:
            if waitRole in member.roles:
                await member.remove_roles(waitRole)
            if helpRole in member.roles:
                await member.remove_roles(helpRole)

        await ctx.send('>>> Help Queue Cleared!')



    #@commands.command()
    #async def roles(self, ctx, roleChoice = 'None', mathRoles = MathRoles):
    #    #for roles in (ctx.message.guild.roles): 
    #        #await ctx.send(f'{roles.name}')
    #    if roleChoice == 'None':
    #        num = 1
    #        x = '```Academic Roles:\n\n'
            
    #        for i in mathRoles.values():
    #            #await ctx.send(f'> {i}')
    #            #x = x + i + '\n ' + str(num) + ': '
    #            x = f'{x}{num}: {i} \n'
    #            num += 1
    #        x = x + ' \nSay: "\\roles ##"```'
    #        await ctx.send(f'{x}')
    #    #elif action == 'add':
    #    else:
    #        if int(roleChoice) in mathRoles:
    #            role = discord.utils.get(ctx.message.guild.roles, name = mathRoles.get(int(roleChoice)))
    #            ## add the remove role handler
    #            if role in ctx.message.author.roles:
    #                await ctx.message.author.remove_roles(role)
    #                await ctx.send(f'```Done! Role has been removed :)```')
    #            else:
    #                await ctx.message.author.add_roles(role)
    #                await ctx.send(f'```You have been given the role: {role.name}!```')

    #        else:
    #            await ctx.send(f'{roleChoice} does not correspond to any math role :(')


def setup(client):
    client.add_cog(Help(client))