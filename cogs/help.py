
import discord
from discord.ext import commands, tasks

nextline = """
"""
def split_space(var1) :
    if var1.find(' ') == -1 :
        return ''
    else:
        return var1[var1.find(' ')+1:]

def split_space_list(var):
    _list = []
    while len(var) > 0:
        if ' ' in var:
            _list.append(var[: var.find(' ')])
            var = var[var.find(' ') + 1 :]
        else:
            _list.append(var)
            var = ''
    return _list

async def getHelpCh(g):
    for c in g.text_channels:
        if c.name == 'help-requests':
            return c
    c = await g.create_text_channel('help-requests')
    return c






class Help_Test(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def gethelp(self, ctx, *,subject = 'optional'):
        # Assign role showing that the user is waiting for a helper
        waitRole = discord.utils.get(ctx.message.guild.roles, name = 'WaitingForHelp')
        helpRole = discord.utils.get(ctx.message.guild.roles, name = 'BeingHelped')
        helpers = discord.utils.get(ctx.message.guild.roles, name = 'Helpers')

        help_channel = await getHelpCh(ctx.guild)
        messages = await help_channel.history(limit=20).flatten()
        cont = 1
        for m in messages:
            try:
                s = m.embeds[0].description
                #if s[:s.find('>')+1] == ctx.message.author.mention:
                #    await ctx.send(f'You have already requested help in {s[-22:-1]}.')
                #    cont = 0
                #    break                
                if s[:s.find('>')+1] == ctx.message.author.mention:
                    if helpRole in ctx.message.author.roles or waitRole in ctx.message.author.roles:
                        await ctx.send(f'You have already requested help in {s[-22:-1]}.')
                        cont = 0
                        break
            except:
                pass
        if cont == 1:
            tempDescription = f'{ctx.message.author.mention} has requested help in {ctx.message.channel.mention}.{nextline}'
            #if not ctx.message.content.endswith('-ping off'):
            #    tempDescription += f'{helpers.mention}'
            embed = discord.Embed(
                title = f'**{ctx.message.author}**', 
                color = discord.Color.red(), 
                description = tempDescription )

            # embed.add_field(name = '**Details**', value = split_space(ctx.message.content))
            embed.add_field(name = '**Details**', value = ('None' if (subject == 'optional') else subject))
            #embed.add_field(name = '**Status**', value = 'Waiting')
            embed.set_thumbnail(url = ctx.message.author.avatar_url)
            await help_channel.send(embed = embed)
            await ctx.message.channel.send('Help request has been successfully made. A helper will soon get to you.')
            await ctx.message.author.add_roles(waitRole)


    @commands.command()
    async def endhelp(self, ctx, member : discord.Member = discord.ClientUser):

        waitRole = discord.utils.get(ctx.message.guild.roles, name = 'WaitingForHelp')
        helpRole = discord.utils.get(ctx.message.guild.roles, name = 'BeingHelped')

        help_ch = await getHelpCh(ctx.guild)
        messages = await help_ch.history(limit=20).flatten()

        found = 0

        if(member == discord.ClientUser):
            for m in messages :
                try:
                    s = m.embeds[0].description
                    if s[:s.find('>')+1] == ctx.message.author.mention:
                        found = 1
                        break
                except:
                    pass
            if found == 0:
                #await ctx.send('You do not have any active requests.')
                if helpRole in ctx.message.author.roles or waitRole in ctx.message.author.roles:
                    await ctx.message.author.remove_roles(waitRole)
                    await ctx.message.author.remove_roles(helpRole)
                    await ctx.send('>>> ✅')
                else:
                    await ctx.send('You do not have any active requests.')
                    

            else:
                await m.add_reaction('💯')
                await ctx.send('>>> ✅')
                await ctx.message.author.remove_roles(waitRole)
                await ctx.message.author.remove_roles(helpRole)

                # change color of embed
                embed = m.embeds[0]
                embed2 = discord.Embed(title = embed.title, description=embed.description, color = discord.Colour.green())
                embed2.set_thumbnail(url = ctx.message.author.avatar_url)
                embed2.set_footer(text = f'Request has been resolved.', icon_url = ctx.message.author.avatar_url)
                await m.edit(embed = embed2)
        else:
            for m in messages :
                try:
                    s = m.embeds[0].description
                    if s[:s.find('>')+1] == member.mention:
                        found = 1
                        break
                except:
                    pass
            if found == 0:
                if helpRole in member.roles or waitRole in member.roles:
                    await ctx.send('>>> ✅')
                    await member.remove_roles(waitRole)
                    await member.remove_roles(helpRole)
                else:
                    await ctx.send('Member does not have any active requests.')
            else:
                await m.add_reaction('💯')
                await ctx.send('>>> ✅')
                await member.remove_roles(waitRole)
                await member.remove_roles(helpRole)

                # change color of embed
                embed = m.embeds[0]
                embed2 = discord.Embed(title = embed.title, description=embed.description, color = discord.Colour.green())
                embed2.set_thumbnail(url = member.avatar_url)
                embed2.set_footer(text = f'Request has been resolved.', icon_url = member.avatar_url)
                await m.edit(embed = embed2)

    @commands.command()
    async def starthelp(self, ctx, member : discord.Member):
        waitRole = discord.utils.get(ctx.message.guild.roles, name = 'WaitingForHelp')
        helpRole = discord.utils.get(ctx.message.guild.roles, name = 'BeingHelped')
        #if member == 'none':
        #    await ctx.send('Please provide member')
        #    pass
        #else:
        help_ch = await getHelpCh(ctx.guild)
        messages = await help_ch.history(limit=20).flatten()
        found = 0
        for m in messages :
            try:
                s = m.embeds[0].description
                if s[:s.find('>')+1] == member.mention:
                    found = 1
                    break
            except:
                pass
        if not (helpRole in member.roles or waitRole in member.roles):
            await ctx.send(f'{member.mention} has not requested assistance. {member.nick} must enter `\gethelp <description`')
        else:
            embed = m.embeds[0]
            embed2 = discord.Embed(title = embed.title, description=embed.description, color = discord.Colour.orange())
            embed2.set_thumbnail(url = member.avatar_url)
            #embed2.add_field(embed.fields[0])
            embed2.set_footer(text = f'{ctx.message.author.name} is now providing assistance.', icon_url = ctx.message.author.avatar_url)
            await m.edit(embed = embed2)
            await ctx.send('>>> ✅')
            await member.add_roles(helpRole)
            await member.remove_roles(waitRole)


    @commands.command()
    async def refreshrequest(self, ctx):
        help_ch = await getHelpCh(ctx.guild)
        messages = await help_ch.history(limit=20).flatten()
        found = 0
        for m in messages :
            try:
                s = m.embeds[0].description
                if s[:s.find('>')+1] == ctx.message.author.mention:
                    found = 1
                    break
            except:
                pass
        if found == 0:
            await ctx.send('You do not have any requests to refresh.')
        else:
            mc = m.content
            me = m.embeds[0]
            me2 = discord.Embed(title = me.title, description = me.description, color = discord.Color.red())
            me2.set_thumbnail(url = ctx.message.author.avatar_url)
            me2.add_field(me.fields[0])
            await m.delete()
            await help_ch.send(content=mc, embed = me)
            await ctx.send('Your help request has been refreshed.')

    @commands.command()
    async def cancelrequest(self, ctx):
        # Remove any assigned help request roless
        waitRole = discord.utils.get(ctx.message.guild.roles, name = 'WaitingForHelp')
        helpRole = discord.utils.get(ctx.message.guild.roles, name = 'BeingHelped')
        
        await ctx.message.author.remove_roles(waitRole)
        await ctx.message.author.remove_roles(helpRole)
        # end_roles


        help_ch = await getHelpCh(ctx.guild)
        messages = await help_ch.history(limit=20).flatten()
        found = 0
        for m in messages :
            try:
                s = m.embeds[0].description
                if s[:s.find('>')+1] == ctx.message.author.mention:
                    found = 1
                    break
            except:
                pass
        if found == 0:
            await ctx.send('You do not have any active requests to cancel.')
        else:
            await m.delete()
            await ctx.send('Your help request has been canceled.')

    #elif msg.content.startswith(r'\help'):
    #    await msg.channel.send("help message for christ's sake.")

def setup(client):
    client.add_cog(Help_Test(client))