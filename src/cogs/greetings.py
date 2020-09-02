import datetime

import discord
from discord import Embed
from discord.ext import commands
from random import choice
import json
import requests


class Greetings(commands.Cog):
    """
    Fun commands to try
    """

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
        """Tells math jokes"""
        with open('src/cogs/jokes.json') as joke_file:
            jokes = json.load(joke_file)
            q = choice(list(jokes.keys()))
            await ctx.send('Q: ***{}***\nA: {}'.format(q, jokes[q]))

    @commands.command()
    async def meme(self, ctx):
        """Sends math memes"""
        with open('src/cogs/memes.txt', 'r') as memes:
            await ctx.send(choice(memes.read().split('\n')))

    @commands.command()
    async def status(self, ctx):
        """Shows status of Discord"""
        URL = 'https://srhpyqt94yxb.statuspage.io/api/v2/incidents/unresolved.json'
        incidents = requests.get(URL).json()["incidents"]

        if len(incidents) == 0:
            await ctx.send('Discord is not f--ked')
        else:
            await ctx.send('Discord is f--ked')

            for incident in incidents:
                embed = Embed(title='Incident name: ' + incident['name'], url=incident['shortlink'], description='Services affected')

                for component in incident['components']:
                    embed.add_field(name=component['name'], value=component['description'])

                await ctx.send(embed=embed)
