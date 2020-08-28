import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')


@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))

@ bot.event 
async def on_member_remove(member): 
    print(f'{member} has left the server!! >:c') 
    
@bot.command() 
async def ping(ctx): 
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms') 

@bot.command() 
async def solve(ctx, eq): 
    await ctx.send('{}={}'.format(eq, eval(eq))) 

if __name__ == '__main__':
    token = os.getenv('TOKEN')
    if token:
        bot.run(token)
    else:
        with open('bot_token.txt') as bot_token_file:
            token = bot_token_file.readline()

            bot.run(token)
