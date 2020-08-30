import discord
from discord.ext import commands
from random import choice
import json


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}!! >:D'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('{0.mention} had left the server!! >:c'.format(member))

    @commands.command()
    async def joke(self, ctx):
        with open('jokes.json') as joke_file:
            jokes = json.load(joke_file)
            q = choice(list(jokes.keys()))
            await ctx.send('{}\n{}'.format(q, jokes[q]))

    @commands.command()
    async def meme(self, ctx):
        pass
