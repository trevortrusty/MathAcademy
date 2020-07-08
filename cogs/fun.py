import discord
from discord.ext import commands, tasks

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

   
    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    # Echo
    @commands.command()
    @commands.has_any_role('Owners', 'Big Brain Moderator', 'Admin')
    async def echo(self, ctx, *, message): ## Repeats message given by user calling the command
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'{message}')



    @commands.command()
    @commands.has_any_role('Owners', 'Bot Master')
    async def christmas(self, ctx): ## Repeats message given by user calling the command
        await ctx.channel.purge(limit = 1)
        embed = discord.Embed(
            title = '**Merry Christmas**!!',
            color = discord.Color.red(),
            description = 'from the Math Academy staff team',
            )
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/610176122214416388/659261013471789066/g3873.png')
        embed.set_footer(text = 'in soviet Russia, presents unwrap you!', icon_url = 'https://p7.hiclipart.com/preview/263/706/356/gift-card-business-christmas-gift-gift.jpg')
        await ctx.send(embed = embed)
def setup(client):
    client.add_cog(Fun(client))