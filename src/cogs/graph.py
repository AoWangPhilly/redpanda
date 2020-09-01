import discord
from discord.ext import commands
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import *


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

    @commands.command()
    async def graph3d(self, ctx, *, eq: parse_eq):
        """Graphs equations in 3d"""
        p1 = plot3d(eq, show=False)
        p1.save(self.graph_location)
        await ctx.send(file=discord.File(self.graph_location))

    @commands.command(name='pgraph')
    async def p_graph(self, ctx, x: parse_eq, y: parse_eq):
        """
        Graph parametric equations
        Uses a single parameter
        """
        p1 = plot_parametric(x, y)
        p1.save(self.parametric_graph_location)
        await ctx.send(file=discord.File(self.parametric_graph_location))

    @commands.command(name='pgraph3dline')
    async def p_graph_line(self, ctx, x: parse_eq, y: parse_eq, z: parse_eq):
        """
        Graph 3d parametric equations in line form
        Uses a single parameter
        """
        p1 = plot3d_parametric_line(x, y, z)
        p1.save(self.parametric_graph_location)
        await ctx.send(file=discord.File(self.parametric_graph_location))

    @commands.command(name='pgraph3dsurface')
    async def p_graph_surface(self, ctx, x: parse_eq, y: parse_eq, z: parse_eq):
        """
        Graph 3d parametric equations in surface form
        Uses two parameters
        """
        p1 = plot3d_parametric_surface(x, y, z)
        p1.save(self.parametric_graph_location)
        await ctx.send(file=discord.File(self.parametric_graph_location))
