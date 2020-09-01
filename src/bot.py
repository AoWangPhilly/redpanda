'''
description: a Discord bot that solves simple arthimetic problems 
to complex multivariate calculus probelms, graphs single variable equations,
and tells jokes.
'''

import os
import discord
from discord.ext import commands

# noinspection PyUnresolvedReferences
from cogs.greetings import Greetings

# noinspection PyUnresolvedReferences
from cogs.vector import Vector

# noinspection PyUnresolvedReferences
from cogs.calculus import Calculus

# noinspection PyUnresolvedReferences
from cogs.graph import Graph

from cogs.plane import Plane
bot = commands.Bot(command_prefix='!')

# Adding different cogs for included functionality 
bot.add_cog(Greetings(bot))
bot.add_cog(Vector(bot))
bot.add_cog(Calculus(bot))
bot.add_cog(Graph(bot))
bot.add_cog(Plane(bot))

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('with your mum, panda panda! 🐼'))
    print('Logged on as {0}!'.format(bot.user))


# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('Please pass in all required arguments!! @.@')
#     elif isinstance(error, commands.CommandNotFound):
#         await ctx.send('Invalid command used!! >.<')
#     elif isinstance(error, commands.MissingPermissions):
#         await ctx.send('You don\'t got the power!! :D')


@bot.command()
async def ping(ctx):
    """
    Returns pong!
    """
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms')


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    """
    Clear n-amount of messages
    """
    await ctx.channel.purge(limit=amount)


if __name__ == '__main__':
    token = os.getenv('TOKEN')
    if token:
        bot.run(token)
    else:
        with open('bot_token.txt') as bot_token_file:
            token = bot_token_file.readline()
            bot.run(token)
