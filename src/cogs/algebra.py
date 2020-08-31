import discord
from discord.ext import commands
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot


def parse_eq(eq):
    eq = eq.replace('^', '**').replace('e', 'E')
    return parse_expr(eq)


class Algebra(commands.Cog):
    """
    Contains various algebra tools
    """

    def __init__(self, bot):
        self.bot = bot
        self.file_location = 'temp/graph.png'

    @commands.command()
    async def graph(self, ctx, *, eq: parse_eq):
        """Graphs simple equations"""
        p1 = plot(eq, show=False)
        p1.save(self.file_location)
        await ctx.send(file=discord.File(self.file_location))
