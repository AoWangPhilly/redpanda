import os
import sympy
import discord
from discord.ext import commands
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))


@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server!! >:D')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server!! >:c')


@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms')


@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def integrate(ctx, *, eq):
    try:
        eq = parse_expr(eq.replace('^', '**'))
        sympy.preview(sympy.integrate(eq), viewer='file',
                filename='output.png', dvioptions=['-D', '200'])
        await ctx.send(file=discord.File('output.png'))
    except: 
        await ctx.send('Error! Try again :<')


@bot.command()
async def derive(ctx, *, eq):
    try:
        eq = parse_expr(eq.replace('^', '**'))
        sympy.preview(sympy.diff(eq), viewer='file',
                filename='output.png', dvioptions=['-D', '200'])
        await ctx.send(file=discord.File('output.png'))
    except: 
        await ctx.send('Error! Try again :<')


@bot.command()
async def graph(ctx, *, eq):
    eq = parse_expr(eq.replace('^', '**'))
    p1 = plot(eq, show=False)
    p1.save('graph.png')
    await ctx.send(file=discord.File('graph.png'))


if __name__ == '__main__':
    token = os.getenv('TOKEN')
    if token:
        bot.run(token)
    else:
        with open('bot_token.txt') as bot_token_file:
            token = bot_token_file.readline()
            print(sympy.__version__)
            bot.run(token)
