import os

from discord.ext import commands

bot = commands.Bot(command_prefix='>')


@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))


if __name__ == '__main__':
    token = os.getenv('TOKEN')
    if token:
        bot.run(token)
    else:
        with open('bot_token.txt') as bot_token_file:
            token = bot_token_file.readline()

            bot.run(token)
