import discord
from discord.ext import commands
import axiomathbf
import sympy
from utility.math_parser import parse_eq

class Extrema(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file_location = 'temp/output.png'
    
    @commands.command()
    async def relative(self, ctx, func: parse_eq):
        await ctx.send(axiomathbf.Extrema(func).get_relative())
    
    @commands.command()
    async def absolute(self, ctx, func: parse_eq, p1, p2, p3):
        pass