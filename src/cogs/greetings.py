import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}!! >:D'.format(member))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('{0.mention} had left the server!! >:c'.format(member))
    
    @commands.command()
    async def joke(self, ctx):
        pass

    @commands.command()
    async def meme(self, ctx):
        pass

