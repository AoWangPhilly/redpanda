import discord
from discord.ext import commands
import sympy

class Plane(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file_location = 'temp/output.png'
    