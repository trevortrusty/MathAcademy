import discord
from discord.ext import commands, tasks

tc_table = {}
vc_table = {}

class Help_Beta(commands.Cog):

    def __init__(self, client):
        self.client = client
        

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        help_cat = self.client.get_channel(652486518266658846)
        voice_channel = self.client.get_channel(705573614593769472)

        if before.channel is not voice_channel and after.channel is voice_channel:
            tc_table[member.id] = await help_cat.create_text_channel(f'{member.name} session')            
            await tc_table[member.id].send('Welcome to MathAcademy bot 2.0 beta. Your help session has been created, and will disapear when you leave the voice channel')
            
        elif before.channel is voice_channel and after.channel is not voice_channel:
            print('elif statement executed')
            await tc_table[member.id].delete()

        #        if(before.channel is voice_channel and after.channel is vc_table[member.id]):
        #    pass
        #elif(before.channel is vc_table[member.id] and after.channel is not vc_table[member.id]):
        #    await tc_table[member.id].delete()
        #    await vc_table[member.id].delete()
        #elif before.channel is not voice_channel and after.channel is voice_channel:
        #    tc_table[member.id] = await help_cat.create_text_channel(f'{member.name} session')
        #    vc_table[member.id] = await help_cat.create_voice_channel(f'{member.name} vc')
        #    await tc_table[member.id].send('Welcome to MathAcademy bot 2.0 beta. Your help session has been created, and will disapear when you leave the voice channel')      
        #elif before.channel is voice_channel and after.channel is not voice_channel:
        #    print('elif statement executed')
        #    await tc_table[member.id].delete()

    @commands.command()
    @commands.has_any_role('Owners', 'Admin', 'Moderator', 'Helpers', 'Tutor')
    async def forceclose(self, ctx):
        help_cat = self.client.get_channel(652486518266658846)
        if ctx.channel.category is help_cat:
            await ctx.channel.delete()
        else:
            await ctx.send("Not a help portal created channel")

def setup(client):
    client.add_cog(Help_Beta(client))