import discord
from discord.ext import commands
import sympy
import axiomathbf

class ChainRule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file_location = 'temp/vector.png'
