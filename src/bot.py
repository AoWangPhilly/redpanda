import os
import discord
from discord.ext import commands
from cogs.greetings import Greetings
from cogs.calculus import Calculus

bot = commands.Bot(command_prefix='!')
bot.add_cog(Greetings(bot))
bot.add_cog(Calculus(bot))


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('with your mum, panda panda! 🐼'))
    print('Logged on as {0}!'.format(bot.user))


@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms')


@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

if __name__ == '__main__':
    token = os.getenv('TOKEN')
    if token:
        bot.run(token)
    else:
        with open('bot_token.txt') as bot_token_file:
            token = bot_token_file.readline()
            bot.run(token)
