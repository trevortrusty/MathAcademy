import discord
from discord.ext import commands, tasks
import asyncio
from itertools import cycle


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client
    # BotAccount = 0
    #thing = cycle([discord.Game('\\roles'), discord.Watching(name='Organic Chemistry Tutor', url = 'https://www.twitch.tv/pewdiepie/')])
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Start your engines.') 
        while True:
            await self.client.change_presence(activity=discord.Game('\\roles'))
            await asyncio.sleep(4)
            await self.client.change_presence(activity=discord.Streaming(name='PewDiePie', url = 'https://www.twitch.tv/pewdiepie/'))       
            await asyncio.sleep(4)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('/gethelp'):
            await message.channel.send('>>> Warning: I think you may have meant to type ```\gethelp``` :)')  
          
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        systemChannel = self.client.get_channel(698664722869911677)
        botChannel = self.client.get_channel(698664724426129421)
        rulesChannel = self.client.get_channel(698664722425184273)
        #role = discord.utils.get(rulesChannel.guild.roles, name = 'rules')
        #await member.add_roles(role) #commented out until bots are 24/7 hosted
        #await asyncio.sleep(600)
        #member.remove_role('Read The Rules!!!')
        #await systemChannel.send(f'>>> Welcome to MathAcademy, {member.mention}!\n🚗🚗Type \\roles in {botChannel.mention} to get a list of math roles, and then use the role\'s number to assign a role. Also, don\'t forget to read {rulesChannel.mention}!\nHow to get help: Go to a Roman Numeral marked help channel, and type `\gethelp <subject>`.')

        #welcome = discord.Embed(
        #    title = f'Welcome to MathAcademy, {member.name}!',
        #    description = f'🚗🚗Type \\roles in {botChannel.mention} to get a list of math roles, and then use the role\'s number to assign a role. Also, don\'t forget to read {rulesChannel.mention}!\nHow to get help: Go to a Roman Numeral marked help channel, and type `\gethelp <subject>`.',
        #    color = discord.Color.blue()
        #    )
        welcome = discord.Embed(
            title = f'Welcome to MathAcademy, {member.name}!',
            description = f'🚗🚗Type \\roles in {botChannel.mention} to get a list of math roles, and then use the role\'s number to assign a role. Also, don\'t forget to read {rulesChannel.mention}!\nHow to get help: Go to a Roman Numeral marked help channel, and type `\gethelp <subject>`.',
            color = discord.Color.blue()
            )
        welcome.set_footer(text = 'We\'re glad you\'re here. Type \\roles for a list of commands', icon_url = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/microsoft/209/smiling-face-with-open-mouth-and-smiling-eyes_1f604.png')
        welcome.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/610176122214416388/659261013471789066/g3873.png')
        await systemChannel.send(embed = welcome)


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 657363665862787072:
            print(payload.emoji.name)
            if payload.emoji.name == '☑️':
                rulesChannel = self.client.get_channel(600850050825846806)
                role = discord.utils.get(rulesChannel.guild.roles, name = 'rules')
                member = discord.utils.find(lambda m : m.id == payload.user_id, rulesChannel.guild.members)
                await member.remove_roles(role)
            ## Find a role corresponding to the Emoji name.
            #guild_id = payload.guild_id
            #guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

            #role = discord.utils.find(lambda r : r.name == payload.emoji.name, guild.roles)

            #if role is not None:
            #    print(role.name + " was found!")
            #    print(role.id)
            #    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            #    await member.add_roles(role)
            #    print("done") 
                

def setup(client):
    client.add_cog(Events(client))