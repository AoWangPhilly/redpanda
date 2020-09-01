import discord
from discord.ext import commands
from sympy import plot_parametric
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot


def parse_eq(eq):
    eq = eq.replace('^', '**').replace('e', 'E')
    return parse_expr(eq)


class Graph(commands.Cog):
    """
    Contains various algebra tools
    """

    def __init__(self, bot):
        self.bot = bot
        self.graph_location = 'temp/graph.png'
        self.parametric_graph_location = 'temp/parametric_graph.png'

    @commands.command()
    async def graph(self, ctx, *, eq: parse_eq):
        """Graphs simple equations"""
        p1 = plot(eq, show=False)
        p1.save(self.graph_location)
        await ctx.send(file=discord.File(self.graph_location))

    @commands.command(name='pgraph')
    async def p_graph(self, ctx, x: parse_eq, y: parse_eq):
        """Graph parametric equations"""
        p1 = plot_parametric(x, y)
        p1.save(self.graph_location)
        await ctx.send(file=discord.File(self.parametric_graph_location))
