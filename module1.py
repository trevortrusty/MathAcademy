import discord

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

with open('token.txt') as file:
    token = file.read()

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @client.event
    async def on_ready():
        print(f'Logged in as : {client.user}{nextline}Currently joined guilds - ')
        for g in client.guilds:
            print(f'{g.id} - {g.name}')
            found = 0
            for x in g.text_channels:
                if x.name == 'help-requests':
                    found = 1
                    break
            if found ==0:
                channel = await g.create_text_channel('help-requests')
                await channel.send('HELP MESSAGE BLAH BLAH')

    @client.event
    async def on_guild_join(g):
        print(f'{nextline}  Joined new guild - {nextline}     {g.id} - {g.name}{nextline}')


    @client.event
    async def on_message(msg):

        print(f'[{msg.guild.id}][{msg.guild.name}][{msg.author}] : {msg.content}')

        if msg.content.startswith(r'\needhelp'):
            help_channel = await getHelpCh(msg.guild)
            messages = await help_channel.history(limit=20).flatten()
            cont = 1
            for m in messages:
                try:
                    s = m.embeds[0].description
                    if s[:s.find('>')+1] == msg.author.mention:
                        await msg.channel.send(f'You have already requested help in {s[-22:-1]}.')
                        cont = 0
                        break
                except:
                    pass
            if cont == 1:
                embed = discord.Embed(title = f'**{msg.author}**', color = discord.Color.red(), description = f'{msg.author.mention} has requested help in {msg.channel.mention}.{nextline}' )
                embed.add_field(name = '**Details**', value = split_space(msg.content))
                embed.set_thumbnail(url = msg.author.avatar_url)
                await help_channel.send(embed = embed)
                await msg.channel.send('Help request has been successfully made. A helper will soon get to you.')

        elif msg.content.startswith(r'\helping'):
            cmd = msg.mentions
            if cmd == []:
                await msg.channel.send('Helping who?')
            elif len(cmd) > 1:
                await msg.channel.send('Help one person at a time please.')
            else:
                cmd = cmd[0]
                help_ch = await getHelpCh(msg.guild)
                messages = await help_ch.history(limit=20).flatten()
                found = 0
                for m in messages :
                    try:
                        s = m.embeds[0].description
                        if s[:s.find('>')+1] == cmd.mention:
                            found = 1
                            break
                    except:
                        pass
                if found == 0:
                    await msg.channel.send('The user is not requesting for help. but help em anyways i guess.(not really)')
                else:
                    embed = m.embeds[0]
                    embed2 = discord.Embed(title = embed.title, description=embed.description, color = discord.Colour.green())
                    embed2.set_thumbnail(url = msg.author.avatar_url)
                    embed2.add_field(embed.fields[0])
                    embed2.set_footer(text = f'Being helped by {msg.author.name}.', icon_url = msg.author.avatar_url)
                    await m.edit(embed = embed2)
                    await msg.channel.send('Request has been edited.')

        elif msg.content.startswith(r'\refreshrequest'):
            help_ch = await getHelpCh(msg.guild)
            messages = await help_ch.history(limit=20).flatten()
            found = 0
            for m in messages :
                try:
                    s = m.embeds[0].description
                    if s[:s.find('>')+1] == msg.author.mention:
                        found = 1
                        break
                except:
                    pass
            if found == 0:
                await msg.channel.send('You do not have any requests to refresh.')
            else:
                mc = m.content
                me = m.embeds[0]
                me2 = discord.Embed(title = me.title, description = me.description, color = discord.Color.red())
                me2.set_thumbnail(url = msg.author.avatar_url)
                me2.add_field(me.fields[0])
                await m.delete()
                await help_ch.send(content=mc, embed = me)
                await msg.channel.send('Your help request has been refreshed.')

        elif msg.content.startswith(r'\cancelrequest'):
            help_ch = await getHelpCh(msg.guild)
            messages = await help_ch.history(limit=20).flatten()
            found = 0
            for m in messages :
                try:
                    s = m.embeds[0].description
                    if s[:s.find('>')+1] == msg.author.mention:
                        found = 1
                        break
                except:
                    pass
            if found == 0:
                await msg.channel.send('You do not have any active requests to cancel.')
            else:
                await m.delete()
                await msg.channel.send('Your help request has been canceled.')

        elif msg.content.startswith(r'\help'):
            await msg.channel.send("help message for christ's sake.")


    # @client.event
    # async def on_reaction_add(reaction, user):
    #     msg = reaction.message
    #     if msg.channel.name == 'help-requests' and msg.author == client.user:
    #         if reaction.emoji == 'white_check_mark' and user.guild_permissions.manage_messages:
    #             await msg.delete()
    #     print(reaction.emoji)

    @client.event
    async def on_member_remove(member):
        help_ch = await getHelpCh(member.guild)
        messages = await help_ch.history(limit=20).flatten()
        for m in messages:
            try:
                s = m.embeds[0].description
                if s[:s.find('>')+1] == member.mention:
                    m.delete()
                    break
            except:
                pass
    client.run(token)
